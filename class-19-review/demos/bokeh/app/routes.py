from flask import Flask, request, render_template, redirect, url_for, session, abort, flash, session
from sqlalchemy.exc import IntegrityError

from . import app
from .forms import SearchForm, HiddenCompanyForm, PortfolioForm, DeleteCompany, AuthForm
from .auth import login_required
from .models import db, Company, Portfolio
from .charts import make_5y_stock_chart, make_5y_vwap_chart

from json import JSONDecodeError

from .route_helpers import fetch_company_data, make_db_record, make_portfolio_db_record, delete_company_from_db


@app.route('/')
def home():
    return render_template('pages/home.html')


@app.route('/search', methods=['GET', 'POST'])
@login_required
def search():
    """ function for /search route.
    get - directly visiting search page to make a search. renders search page
    template.
        - if they don't yet have a portfolio, redirect to /portfolio

    post - they have submitted the form on the search page.
         - first checks db to see if company is already added.
         - if not, makes api call to get company info.
         - if no issues with above, saves api data to context and
          sends to /company
         - if there are issues, or info already in db, redirects to search
           with flashed message.
    """
    data = Portfolio.query.filter(Portfolio.account_id == session['account_id']).first()

    if data is None:
        flash('Please make a portfolio')
        return redirect(url_for('.portfolio'))

    form = SearchForm()

    if form.validate_on_submit():
        company = form.data['company']

        res = fetch_company_data(company)

        if res:
            session['context'] = res
            return redirect(url_for('.company'))

        flash('Company was not found.')
        return redirect(url_for('.search'))

    return render_template('pages/search.html', form=form)


@app.route('/portfolio', methods=['GET', 'POST'])
@login_required
def portfolio():
    """ function for /portfolio route. get only.
    displays company information from database that user has added.
    if there is a db error flashes a message.
    """
    form = PortfolioForm()
    delete_form = DeleteCompany()

    if form.validate_on_submit():
            portfolio = make_portfolio_db_record(form.data['name'], session.get('account_id'))
            if portfolio:
                flash('Portfolio created!')
                return redirect(url_for('.search'))

            flash('there was an issue making your portfolio')
            return redirect(url_for('.portfolio'))

    data = Portfolio.query.filter(Portfolio.account_id == session['account_id']).first()
    if data is None:
        return render_template(
            'pages/portfolio.html',
            companies=None,
            portfolio=False,
            form=form)

    try:
        portfolios = {}
        for portfolio in Portfolio.query.filter(Portfolio.account_id == session['account_id']).all():
            portfolios[portfolio.id] = portfolio.name

        account_portfolios = Portfolio.query.filter(Portfolio.account_id == session['account_id']).all()
        cat_ids = [c.id for c in account_portfolios]

        companies = Company.query.filter(Company.portfolio_id.in_(cat_ids)).all()

    except IntegrityError:
        flash('There was an issue getting your portfolio from the database.')
        all_companies = []
        portfolios = None

    return render_template(
        'pages/portfolio.html',
        all_companies=companies,
        portfolios=portfolios,
        portfolio=True,
        form=form,
        delete_form=delete_form)


@app.route('/company', methods=['GET', 'POST'])
@login_required
def company():
    """ function for /company route
    get - they have visited the page directly (or by redirect).
        - if session data is found for company data, renders company data on
          page.
        - if no session data is found, redirect to search page

    post - if they have
         - adds record to db and redirects to portfolio
         - if there is an issue adding to db, flashes message and
           redirects to /company
    """
    form = HiddenCompanyForm()

    if form.validate_on_submit():
        try:
            company = form.data
            data = db.session.query(Company) \
                .filter(Company.symbol == company['symbol']) \
                .filter(Company.portfolio_id == form.data['portfolio_id']) \
                .first()

            if not data:
                success = make_db_record(company)

                if success:
                    portfolio = Portfolio.query.filter(Portfolio.account_id == form.data['portfolio_id']).first()
                    flash(f'Added {company["companyName"]} to your portfolio!')
                    return redirect(url_for('.portfolio'))

            else:
                flash(f'{company["companyName"]} is already in that portfolio!')
                return redirect(url_for('.company'))

        except IntegrityError:
            flash(f'There was an issue adding to your portfolio')
            return redirect(url_for('.search'))

    if session.get('context') is not None:

        company = session['context']
        chart_script, chart_div = make_5y_stock_chart(company['symbol'])
        chart_vwap_script, chart_vwap_div = make_5y_vwap_chart(company['symbol'])
        return render_template(
            'pages/company.html',
            company=company,
            form=form,
            chart_script=chart_script,
            chart_div=chart_div,
            chart_vwap_div=chart_vwap_div,
            chart_vwap_script=chart_vwap_script
            )

    flash('Search expired. Please try your search again.')
    return redirect(url_for('.search'))


@app.route('/delete-company', methods=['POST'])
@login_required
def delete_company():
    """when they click "delete company" on the porfolio """
    form = DeleteCompany()

    if form.validate_on_submit():
        company_id = form.data['company_id']
        portfolio_id = form.data['portfolio_id']
        deleted = delete_company_from_db(company_id, portfolio_id)
        if deleted:
            flash('Company was deleted')
            return redirect(url_for('.portfolio'))

        flash('issue deleting company')
        return redirect(url_for('.portfolio'))

    abort(404)


@app.route('/cancel-company', methods=['POST'])
@login_required
def cancel_submit():
    """
    function for /cancel-company route. This only happens when they click
    "cancel" on the add a company view
    """
    flash('Company was not added.')
    return redirect(url_for('.search'))


@app.route('/stock-data/<company>', methods=['GET'])
@login_required
def stock_data(company=None):
    """ function for a page wheere you can see charts for a given company """
    if company is None:
        abort(404)

    chart_script, chart_div = make_5y_stock_chart(company)
    chart_vwap_script, chart_vwap_div = make_5y_vwap_chart(company)

    return render_template(
        'pages/stock_data.html',
        company=company,
        chart_script=chart_script,
        chart_div=chart_div,
        chart_vwap_div=chart_vwap_div,
        chart_vwap_script=chart_vwap_script
    )
