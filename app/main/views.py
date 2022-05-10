from flask import render_template, url_for, redirect, request, flash, abort
from app import db, photos
from . import main
from .forms import NewPitchForm, CommentForm
from ..models import Pitches, Comments, Reactions, Categories, Users
from flask_login import login_required, current_user
from sqlalchemy import desc


@main.route('/', methods=['GET', 'POST'])
@login_required
def index():
    # Get all pitches in db
    categories = Categories.query.all()
    all_pitches = Pitches.query.order_by(desc(Pitches.posted_on))
    return render_template('index.html', pitches=all_pitches, categories=categories)


@main.route('/add', methods=["GET", "POST"])
@login_required
def add_pitch():
    # Get all categories from db
    all_categories_list = Categories.query.all()
    choices = []
    for category in all_categories_list:
        choices.append(category.category_name)

    form = NewPitchForm()
    # Submission handling
    if request.method == "POST" and form.validate_on_submit():
        category = form.category.data
        pitch = form.pitch.data

        # if chooses category is in the db
        if category in choices:
            new_pitch = Pitches(pitch_content=pitch, category_id=int(choices.index(category)) + 1,
                                user_id=current_user.user_id)
            db.session.add(new_pitch)
            db.session.commit()
            return redirect(url_for('main.index'))

    return render_template('add-pitch.html', form=form)


@main.route('/comment/<pitch_id>', methods=["GET", "POST"])
@login_required
def add_comment(pitch_id):
    comment_form = CommentForm()

    pitch_comments = Pitches.query.filter_by(pitch_id=pitch_id).first()

    if request.method == "POST":
        if comment_form.validate_on_submit():

            comment = comment_form.comment.data
            new_comment = Comments(comment=comment, pitch_id=pitch_id, user_id=current_user.user_id)

            Comments.save_comment(new_comment)

            return redirect(url_for('main.index'))
        else:
            flash('Invalid comment. Remember, BE NICE')

    return render_template('comment.html', form=comment_form, comments=pitch_comments)


@main.route('/category/<category_id>', methods=["GET", "POST"])
@login_required
def single_category(category_id):
    category_name = Categories.query.filter_by(category_id=category_id).first()
    category_pitches = Pitches.query.filter_by(category_id=category_id).all()
    return render_template('single-category.html', pitches=category_pitches, category=category_name)


@main.route('/like/<user_id>/<pitch_id>', methods=["GET", "POST"])
@login_required
def like(pitch_id, user_id):
    new_like = Reactions(reaction=1, user_id=user_id, pitch_id=pitch_id)
    Reactions.save_reaction(new_like)
    return redirect(request.args.get('next') or url_for('main.index'))


@main.route('/dislike/<user_id>/<pitch_id>', methods=["GET", "POST"])
@login_required
def dislike(pitch_id, user_id):
    new_dislike = Reactions(reaction=0, user_id=user_id, pitch_id=pitch_id)
    Reactions.save_reaction(new_dislike)
    return redirect(request.args.get('next') or url_for('main.index'))


@main.route('/profile/<first_name>', methods=["GET", "POST"])
@login_required
def profile(first_name):
    return render_template('profile.html', user=current_user)


@main.route('/user/<user_id>/upload-profile-picture', methods=['POST'])
@login_required
def upload_profile_pic(user_id):
    user = Users.query.filter_by(user_id=user_id).first()

    if 'photo' in request.files:
        filename = photos.save(request.files['photo'])
        path = f'photos/{filename}'
        user.profile_path = path
        db.session.commit()

    return redirect(url_for('main.profile', user_id=user_id))


@main.route('/user/<user_id>/update-profile-picture', methods=['POST'])
@login_required
def update_profile_pic(user_id):
    user = Users.query.filter_by(user_id=user_id).first()

    if user is None:
        abort(404)

    if 'photo' in request.files:
        filename = photos.save(request.files['photo'])
        path = f'photos/{filename}'
        user.profile_path = path
        db.session.commit()

    return redirect(url_for('main.profile', user_id=user_id))
