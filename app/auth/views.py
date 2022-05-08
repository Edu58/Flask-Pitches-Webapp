from flask import render_template
from . import auth
from .forms import LoginForm, SignupForm


@auth.route('/login')
def login():
    form = LoginForm()

    return render_template('login.html', form=form)


@auth.route('/signup')
def signup():
    form = SignupForm()

    return render_template('signup.html', form=form)
