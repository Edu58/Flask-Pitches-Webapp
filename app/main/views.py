from flask import render_template, url_for, redirect, request, flash
from app import db
from . import main
from .forms import NewPitchForm, CommentForm
from ..models import Users, Pitches, Comments, Reactions, Categories
from flask_login import login_required


@main.route('/', methods=['GET', 'POST'])
@login_required
def index():
    # Get all pitches in db
    all_pitches = Pitches.query.all()
    return render_template('index.html', pitches=all_pitches)


@main.route('/add', methods=["GET", "POST"])
@login_required
def add_pitch():
    # Get all categories from db
    all_categories_list = Categories.query.all()
    choices = []
    for category in all_categories_list:
        choices.append(category.category_name)

    print(choices)

    form = NewPitchForm()
    # Submission handling
    if request.method == "POST" and form.validate_on_submit():
        category = form.category.data
        pitch = form.pitch.data

        # if chooses category is in the db
        if category in choices:
            print(choices.index(category))
            new_pitch = Pitches(pitch_content=pitch, category_id=int(choices.index(category)) + 1)
            db.session.add(new_pitch)
            db.session.commit()
            return redirect(url_for('main.index'))

    return render_template('add-pitch.html', form=form)


@main.route('/comment/<user_id>/<pitch_id>', methods=["GET", "POST"])
@login_required
def add_comment(pitch_id, user_id):
    comment_form = CommentForm()

    all_comments = Pitches.query.filter_by(pitch_id=pitch_id).first()

    if request.method == "POST":
        if comment_form.validate_on_submit():

            comment = comment_form.comment.data
            new_comment = Comments(comment=comment, pitch_id=pitch_id, user_id=user_id)

            Comments.save_comment(new_comment)

            return redirect(url_for('main.index'))
        else:
            flash('Invalid comment. Remember, BE NICE')

    return render_template('comment.html', form=comment_form, comments=all_comments)
