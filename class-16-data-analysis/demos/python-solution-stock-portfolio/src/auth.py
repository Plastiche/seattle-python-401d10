from flask import flash, g, redirect, render_template, session, url_for
from .models import db, User, Portfolio
from .forms import AuthForm
from . import app
import functools


def login_required(view):
    """View decorator that redirects anonymous users to the login page.
    """
    @functools.wraps(view)
    def wrapped_view(**kwargs):
        if g.user is None:
            return redirect(url_for('.login'))

        return view(**kwargs)

    return wrapped_view


@app.before_request
def load_logged_in_user():
    """If a user id is stored in the session, load the user object from
    the database into ``g.user``.
    """
    user_id = session.get('user_id')

    if user_id is None:
        g.user = None
    else:
        g.user = User.query.get(user_id)


@app.route('/register', methods=('GET', 'POST'))
def register():
    """
    """
    form = AuthForm()

    if form.validate_on_submit():
        email = form.data['email']
        password = form.data['password']
        error = None

        if not email or not password:
            error = 'Username is required.'
        elif User.query.filter_by(email=email).first() is not None:
            error = 'User {0} is already registered.'.format(email)

        if error is None:
            new_user = User(email=email, password=password)
            db.session.add(new_user)
            db.session.commit()

            user = User.query.filter_by(email=email).first()

            new_portfolio = Portfolio(name='default', user_id=user.id)
            db.session.add(new_portfolio)
            db.session.commit()

            portfolio = Portfolio.query.filter_by(user_id=user.id).first()
            user.portfolio = portfolio
            db.session.commit()

            return redirect(url_for('.login'))

        flash(error)

    return render_template('auth/register.html', form=form)


@app.route('/login', methods=('GET', 'POST'))
def login():
    """
    """
    form = AuthForm()

    if form.validate_on_submit():
        email = form.data['email']
        password = form.data['password']
        error = None

        user = User.query.filter_by(email=email).first()

        if user is None or not User.check_password_hash(user, password):
            error = 'Incorrect email or password.'

        if error is None:
            session.clear()
            session['user_id'] = user.id
            return redirect(url_for('.portfolio_detail'))

        flash(error)

    return render_template('auth/login.html', form=form)


@app.route('/logout')
def logout():
    """
    """
    session.clear()
    return redirect(url_for('.home'))
