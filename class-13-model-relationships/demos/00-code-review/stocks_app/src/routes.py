from flask import render_template, redirect, url_for, flash, session
from .forms import CompanySearchForm, CompanyAddForm
from sqlalchemy.exc import IntegrityError
from json import JSONDecodeError
from .models import db, Company
import requests as req
from . import app
import json


@app.route('/')
def home():
    """
    """
    return render_template('home.html')


@app.route('/search', methods=['GET', 'POST'])
def company_search():
    """
    """
    form = CompanySearchForm()

    if form.validate_on_submit():
        res = req.get(f'https://api.iextrading.com/1.0/stock/{ form.data["symbol"] }/company')
        flash('validated')
        try:
            session['context'] = res.text
            return redirect(url_for('.company_detail'))
        except JSONDecodeError:
            flash('The company you searched for does not exist.')

    flash('The company you searched for does not exist.')
    return render_template('portfolio/search.html', form=form)


@app.route('/company', methods=['GET', 'POST'])
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
        return render_template('portfolio/search.html', form=form)


@app.route('/portfolio')
def portfolio_detail():
    """
    """
    companies = Company.query.all()
    return render_template('portfolio/portfolio.html', companies=companies)
