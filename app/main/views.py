from flask import render_template, url_for, redirect
from . import main
from .forms import NewPitchForm
from ..models import Users, Pitches, Comments, Reactions, Categories


@main.route('/', methods=['GET', 'POST'])
def index():
    return render_template('index.html')
