from ..app.models import Company, Portfolio, Account
from ..app.models import db as _db
from ..app import app as _app
import pytest
import os


@pytest.fixture()
def app(request):
    """Session-wide Testable Flask Application
    """
    _app.config.from_mapping(
        TESTING=True,
        SECRET_KEY=os.environ.get('SECRET_KEY'),
        SQLALCHEMY_DATABASE_URI=os.getenv('TEST_DATABASE_URL'),
        SQLALCHEMY_TRACK_MODIFICATIONS=False,
        WTF_CSRF_ENABLED=False,
    )

    ctx = _app.app_context()
    ctx.push()

    def teardown():
        ctx.pop()

    request.addfinalizer(teardown)
    return _app


@pytest.fixture()
def db(app, request):
    """Session-wide Test Database
    """
    def teardown():
        _db.drop_all()

    _db.app = app
    _db.create_all()

    request.addfinalizer(teardown)
    return _db


@pytest.fixture()
def session(db, request):
    """Creates a new database session for testing
    """
    connection = db.engine.connect()
    transaction = connection.begin()

    options = dict(bind=connection, binds={})
    session = db.create_scoped_session(options=options)

    db.session = session

    def teardown():
        transaction.rollback()
        connection.close()
        session.remove()

    request.addfinalizer(teardown)
    return session


@pytest.fixture()
def account(app, session):
    """
    """
    account = Account(email='default@example.com', password='secret')

    session.add(account)
    session.commit()
    return account


@pytest.fixture()
def portfolio(session, account):
    """
    """
    portfolio = Portfolio(
        name='Default',
        account_id=account.id
    )

    session.add(portfolio)
    session.commit()
    return portfolio


@pytest.fixture()
def company(session, portfolio):
    """
    """
    company = Company(
        portfolio_id=portfolio.id,
        symbol='aaa',
        companyName='aaa',
        exchange='aaa',
        industry='aaa',
        website='aaa',
        description='aaa',
        CEO='aaa',
        issueType='aaa',
        sector='aaa'
    )

    session.add(company)
    session.commit()
    return company
