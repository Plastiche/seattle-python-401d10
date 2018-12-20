# from flask import session
import pytest
from ..app import app as _app
from ..app.route_helpers import fetch_company_data, make_db_record, delete_company_from_db
from ..app.models import Company, Portfolio, Account


def login_for_test(app):
    app.post('/login', data=dict(
        email='default@example.com',
        password='secret'
    ), follow_redirects=True)


# Home Route

def test_home_route_get_status(app):
    """ tests / route status code"""
    rv = app.test_client().get('/')
    assert rv.status_code == 200


def test_home_route_get_content(app):
    """ tests / route content """
    rv = app.test_client().get('/')
    assert b'Stock Portfolio - Home' in rv.data


def test_home_route_incorrect_method(app):
    """ tests / route with wrong method to make sure correct status code
    is given """
    rv = app.test_client().delete('/')
    assert rv.status_code == 405


# # Search Route - get


def test_search_route_get_status(app):
    """tests /search route status code"""
    rv = app.test_client().get('/search', follow_redirects=True)
    print(rv.data)
    assert rv.status_code == 200


def test_search_route_no_login_redirect(app):
    """tests /search route content"""
    rv = app.test_client().get('/search', follow_redirects=True)
    assert b'Stock Portfolio - Login' in rv.data


def test_search_route_get_content(app, session, db, portfolio, account):
    """tests /search route content"""

    with app.test_client() as app:
        login_for_test(app)

        rv = app.get('/search', follow_redirects=True)
        assert b'Stock Portfolio - Search' in rv.data


def test_search_route_incorrect_method(app):
    """ tests /search route with wrong method to make sure correct status code
    is given """
    rv = app.test_client().delete('/search')
    assert rv.status_code == 405


# # Search/company routes


def test_search_route_post_status(app):
    """ tests that /search post route gives correct status"""
    rv = app.test_client().post('/search', data={'symbol': 'aapl'}, follow_redirects=True)
    assert rv.status_code == 200


def test_search_route_post_content(app, session, db, portfolio, account):
    """tests that when searching for something not yet added the correct
    message is shown"""
    with app.test_client() as app:
        login_for_test(app)

        rv = app.post('/search', data={'company': 'msft'}, follow_redirects=True)
        assert b'Company MSFT found!' in rv.data


def test_search_route_post_graphs(app, session, db, portfolio, account):
    """tests that when searching for something not yet added the chart div is
    added to the source HTML """
    with app.test_client() as app:
        login_for_test(app)

        rv = app.post('/search', data={'company': 'msft'}, follow_redirects=True)
        assert b'class="bk-root"' in rv.data


def test_search_route_post_content_not_found(app, session, db, portfolio, account):
    """ tests status code for when searching for something not found in the
    API"""
    with app.test_client() as app:
        login_for_test(app)

        rv = app.post('/search', data={'company': 'madfada'}, follow_redirects=True)
        assert b'Company was not found.' in rv.data


def test_company_route_no_session(app, session, db, portfolio, account):
    """ Tests company route when no search has been made to make sure that
    user is redirected as expected """
    with app.test_client() as app:
        login_for_test(app)

        rv = app.get('/company', follow_redirects=True)
        assert b'Search expired. Please try your search again.' in rv.data

# # Portfolio Route


def test_portfolio_route_status_code(app):
    """ tests portfolio page to make sure correct status code is sent"""
    rv = app.test_client().get('/portfolio', follow_redirects=True)
    assert rv.status_code == 200


def test_portfolio_route_content(app, session, db, portfolio, account):
    """test content on portfolio route page"""
    with app.test_client() as app:
        login_for_test(app)

        rv = app.get('/portfolio')
        assert b'Stock Portfolio - Your Portfolio' in rv.data


# # cancel-company route


def test_cancel_company_route(app, session, db, portfolio, account):
    """ test cancel-company route content"""
    with app.test_client() as app:
        login_for_test(app)

        rv = app.post('/cancel-company', follow_redirects=True)
        assert b'Company was not added.' in rv.data
        assert b'Stock Portfolio - Search' in rv.data


def test_cancel_company_route_incorrect_method(app, session, db, portfolio, account):
    """ test that it cannot be access by get"""
    with app.test_client() as app:
        login_for_test(app)

        rv = app.get('/cancel-company', follow_redirects=True)
        assert b'404 Not Found' in rv.data


# delete-company route


def test_delete_route_content(app, session, db, portfolio, company, account):
    """ Tests delete route """
    with app.test_client() as app:
        login_for_test(app)

        data = Company.query.first()
        print(data)

        assert data is not None

        app.post('/delete-company', data={'company_id': data.id, 'portfolio_id': account.id}, follow_redirects=True)

        data = Company.query.first()

        assert data is None


# stock_data route


def test_stock_data_route_status_code(app, session, db, portfolio, company, account):
    """ tests status code """
    with app.test_client() as app:
        login_for_test(app)

        rv = app.get('/stock-data/WWW')
        assert rv.status_code == 200


def test_stock_data_route_content(app, session, db, portfolio, company, account):
    """ tests regular content on page """
    with app.test_client() as app:
        login_for_test(app)

        rv = app.get('/stock-data/WWW')
        assert b'class="bk-root"' in rv.data
        assert b'Stock Value History' in rv.data


def test_stock_data_route_404(app, session, db, portfolio, company, account):
    """ tests that a 404 is given when visiting with fake company name """
    with app.test_client() as app:
        login_for_test(app)

        rv = app.get('/stock-data/5432543jkrhjhg32')
        assert rv.status_code == 404


def test_stock_data_route_no_company_404(app, session, db, portfolio, company, account):
    """ tests that a 404 is given when visiting without company name """
    with app.test_client() as app:
        login_for_test(app)

        rv = app.get('/stock-data')
        assert rv.status_code == 404


# register


def test_register_account(app, session, db):
    """test successful register of account"""
    rv = app.test_client().post('/register', data=dict(
        email='default@example.com',
        password='secret'
    ), follow_redirects=True)

    assert b'Registration complete' in rv.data


def test_register_account_exists(app, session, db, account):
    """ test trying to register when the account already exists"""
    rv = app.test_client().post('/register', data=dict(
        email='default@example.com',
        password='secret'
    ), follow_redirects=True)

    assert b'has already been registered' in rv.data


# login


def test_login_no_account(app, session, db):
    """test logging in with no account available"""
    rv = app.test_client().post('/login', data=dict(
        email='default@example.com',
        password='secret'
    ), follow_redirects=True)

    assert b'invalid username or password' in rv.data


def test_login_success(app, session, db, account):
    """test logging in success"""
    rv = app.test_client().post('/login', data=dict(
        email='default@example.com',
        password='secret'
    ), follow_redirects=True)

    assert b'You have logged in successfully' in rv.data


# logout


def test_logout(app, db, session, account):
    with app.test_client() as app:
        login_for_test(app)

        rv = app.get('/logout', follow_redirects=True)

        assert b'You have been logged out' in rv.data


# # errors


def test_404_status_code(app):
    """ tests that 404 is given when navigating to non-existent page """
    rv = app.test_client().get('/asdfa')
    assert rv.status_code == 404


def test_404_content(app):
    """ tests message on page of 404 page """
    rv = app.test_client().get('/asdfa')
    assert b'404 Not Found' in rv.data
