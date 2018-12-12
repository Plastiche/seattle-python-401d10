from flask_wtf import FlaskForm
from wtforms import StringField
from wtforms.validators import DataRequired


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
