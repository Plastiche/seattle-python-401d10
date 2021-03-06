from . import app

from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

from passlib.hash import sha256_crypt

from datetime import datetime as dt


db = SQLAlchemy(app)
migrate = Migrate(app, db)


class Portfolio(db.Model):
    __tablename__ = 'portfolios'

    id = db.Column(db.Integer, primary_key=True)

    name = db.Column(db.String(128))
    date_created = db.Column(db.DateTime, default=dt.now())

    account_id = db.Column(db.ForeignKey('accounts.id'), nullable=False)

    def __repr__(self):
        return '<Portfolio {}>'.format(self.name)


class Company(db.Model):
    __tablename__ = 'companies'

    id = db.Column(db.Integer, primary_key=True)

    portfolio_id = db.Column(db.ForeignKey('portfolios.id'), nullable=False)
    symbol = db.Column(db.String(64), index=True)
    companyName = db.Column(db.String(256), index=True)
    exchange = db.Column(db.String(256))
    industry = db.Column(db.String(256))
    website = db.Column(db.String(256))
    description = db.Column(db.Text)
    CEO = db.Column(db.String(256))
    issueType = db.Column(db.String(256))
    sector = db.Column(db.String(256))

    date_created = db.Column(db.DateTime, default=dt.now())

    def __repr__(self):
        return '<Company {}>'.format(self.companyName)


class Account(db.Model):
    __tablename__ = 'accounts'

    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(256), index=True, nullable=False, unique=True)
    password = db.Column(db.String(256), nullable=False)

    portfolios = db.relationship('Portfolio', backref='user', lazy=True)

    date_created = db.Column(db.DateTime, default=dt.now())

    def __repr__(self):
        return '<Account {}>'.format(self.email)

    def __init__(self, email, password):
        self.email = email
        self.password = sha256_crypt.hash(password)

    @classmethod
    def check_password_hash(cls, account, password):
        if account is not None:
            if sha256_crypt.verify(password, account.password):
                return True

        return False
