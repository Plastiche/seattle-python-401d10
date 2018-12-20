from flask import flash, session
import json
from .models import db, Company, Portfolio
import requests as req
from sqlalchemy.exc import IntegrityError


def fetch_company_data(company):
    """ gets company data from API

    input:
        company - string. symbol for company to search API
    output:
        if company info found - company information dict
        if company not found - None
    """
    try:
        company_data = req.get(f'https://api.iextrading.com/1.0/stock/{company.upper()}/company')
        company_data = json.loads(company_data.text)
        return company_data

    except (json.JSONDecodeError, AttributeError):
        return None


def make_db_record(company_data):
    """
    saves company info to database

    input: company info dict
    output:
        if no errors - returns True
        if errors - returns False
    """
    try:
        company = {
            'portfolio_id': company_data['portfolio_id'],
            'symbol': company_data['symbol'],
            'companyName': company_data['companyName'],
            'exchange': company_data['exchange'],
            'industry': company_data['industry'],
            'website': company_data['website'],
            'description': company_data['description'],
            'CEO': company_data['CEO'],
            'issueType': company_data['issueType'],
            'sector': company_data['sector']
        }

        new_company = Company(**company)
        db.session.add(new_company)
        db.session.commit()

        return True

    except (IntegrityError, json.JSONDecodeError):
        return False

    return False


def make_portfolio_db_record(portfolio_name, account_id=None):
    """ saves new portfolio into db """
    try:
        new_portfolio = Portfolio(
            name=portfolio_name,
            account_id=account_id
        )
        db.session.add(new_portfolio)
        db.session.commit()
        return True

    except IntegrityError:
        return False


def delete_company_from_db(company_id, portfolio_id):
    """ deletes company by id """
    try:
        company = Company.query \
            .filter(Company.id == company_id) \
            .filter(Company.portfolio_id == portfolio_id) \
            .first()
        db.session.delete(company)
        db.session.commit()
        return True
    except IntegrityError:
        return False
