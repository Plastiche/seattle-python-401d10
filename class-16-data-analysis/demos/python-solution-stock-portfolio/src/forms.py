from wtforms import StringField, SelectField, PasswordField
from wtforms.validators import DataRequired
from flask_wtf import FlaskForm
from .models import Portfolio


class CompanySearchForm(FlaskForm):
    """
    """
    symbol = StringField('symbol', validators=[DataRequired()])


class CompanyAddForm(FlaskForm):
    """
    """
    symbol = StringField('symbol', validators=[DataRequired()])
    companyName = StringField('companyName', validators=[DataRequired()])
    exchange = StringField('exchange')
    industry = StringField('industry')
    website = StringField('website')
    description = StringField('description')
    CEO = StringField('CEO')
    issueType = StringField('issueType')
    sector = StringField('sector')
    portfolios = SelectField('portfolio')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.portfolios.choices = [(str(p.id), p.name) for p in Portfolio.query.all()]


class PortfolioAddForm(FlaskForm):
    """
    """
    name = StringField('name', validators=[DataRequired()])


class AuthForm(FlaskForm):
    """
    """
    email = StringField('email', validators=[DataRequired()])
    password = PasswordField('password', validators=[DataRequired()])
