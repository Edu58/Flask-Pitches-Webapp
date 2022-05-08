from flask import render_template, url_for, redirect, request
from app import db
from . import main
from .forms import NewPitchForm
from ..models import Users, Pitches, Comments, Reactions, Categories


@main.route('/', methods=['GET', 'POST'])
def index():
    # Get all pitches in db
    all_pitches = Pitches.query.all()
    return render_template('index.html', pitches=all_pitches)


@main.route('/add', methods=["GET", "POST"])
def add_pitch():
    # Get all categories from db
    all_categories_list = Categories.query.all()
    choices = []
    for category in all_categories_list:
        choices.append(category.category_name)

    print(choices)

    form = NewPitchForm()
    # Submission handling
    if request.method == "POST":
        if form.validate_on_submit():
            category = form.category.data
            pitch = form.pitch.data

            # if chooses category is in the db
            if category in choices:
                new_pitch = Pitches(pitch_content=pitch, category_id=int(choices.index(category)) + 1)
                db.session.add(new_pitch)
                db.session.commit()
                return redirect(url_for('main.index'))

    return render_template('add-pitch.html', form=form)
