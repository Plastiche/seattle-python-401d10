from .forms import CompanySearchForm, CompanyAddForm, PortfolioAddForm
from flask import render_template, redirect, url_for, flash, session, request
from .models import db, Company, Portfolio
from sqlalchemy.exc import IntegrityError
from .auth import login_required
from json import JSONDecodeError
import requests as req
from . import app
import json


@app.add_template_global
def get_portfolios():
    """Allows the use of a function `get_portfolio()` within a template, which returns
    any portfolio records to the template context.
    """
    return Portfolio.query.all()


@app.route('/')
def home():
    """
    """
    return render_template('home.html')


@app.route('/search', methods=['GET', 'POST'])
@login_required
def company_search():
    """
    """
    form = CompanySearchForm()

    if form.validate_on_submit():
        res = req.get(f'https://api.iextrading.com/1.0/stock/{ form.data["symbol"] }/company')

        try:
            session['context'] = res.text
            return redirect(url_for('.company_detail'))
        except JSONDecodeError:
            flash('The company you searched for does not exist.')
            return render_template('portfolio/search.html')

    return render_template('portfolio/search.html', form=form)


@app.route('/company', methods=['GET', 'POST'])
@login_required
def company_detail():
    """
    """
    try:
        context = json.loads(session['context'])
        form = CompanyAddForm(**context)

        if form.validate_on_submit():
            form_data = {
                'symbol': form.data['symbol'],
                'companyName': form.data['companyName'],
                'exchange': form.data['exchange'],
                'industry': form.data['industry'],
                'website': form.data['website'],
                'description': form.data['description'],
                'CEO': form.data['CEO'],
                'issueType': form.data['issueType'],
                'sector': form.data['sector'],
                'portfolio_id': form.data['portfolios']
            }

            try:
                company = Company(**form_data)

                db.session.add(company)
                db.session.commit()
            except IntegrityError:
                flash('You just tried to add a record that already exists.')

            return redirect(url_for('.company_search'))

        return render_template('portfolio/company.html', **context, form=form)

    except JSONDecodeError:
        flash('The company you searched for does not exist.')
        form = CompanySearchForm()
        return render_template('portfolio/search.html', form=form)


@app.route('/portfolio', methods=['GET', 'POST'])
@login_required
def portfolio_detail():
    """
    """
    form = PortfolioAddForm()

    if form.validate_on_submit():
        portfolio = Portfolio(name=form.data['name'], user_id=session['user_id'])
        db.session.add(portfolio)
        db.session.commit()

        return redirect(url_for('.company_search'))

    companies = Company.query.all()

    return render_template('portfolio/portfolio.html', companies=companies, form=form)
