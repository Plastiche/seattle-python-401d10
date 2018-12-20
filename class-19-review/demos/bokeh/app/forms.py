from flask import session
from flask_wtf import FlaskForm
from wtforms import StringField, HiddenField, SelectField, PasswordField
from wtforms.validators import DataRequired

from .models import Portfolio


class SearchForm(FlaskForm):
    company = StringField('company', validators=[DataRequired()])


class HiddenCompanyForm(FlaskForm):
    portfolio_id = SelectField()
    symbol = HiddenField()
    companyName = HiddenField()
    exchange = HiddenField()
    industry = HiddenField()
    website = HiddenField()
    description = HiddenField()
    CEO = HiddenField()
    issueType = HiddenField()
    sector = HiddenField()

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.portfolio_id.choices = [(str(c.id), c.name) for c in Portfolio.query.filter(Portfolio.account_id == session['account_id']).all()]


class PortfolioForm(FlaskForm):
    name = StringField('Portfolio Name', validators=[DataRequired()])


class DeleteCompany(FlaskForm):
    company_id = HiddenField()
    portfolio_id = HiddenField()


class AuthForm(FlaskForm):
    email = StringField('email', validators=[DataRequired()])
    password = PasswordField('password', validators=[DataRequired()])
