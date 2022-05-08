from flask import render_template, url_for, redirect
from . import main
from .forms import NewPitchForm


@main.route('/')
def index():
    form = NewPitchForm()
    return render_template('index.html', form=form)
