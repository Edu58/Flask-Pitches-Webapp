from app import db, login_manager
from datetime import datetime
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin


class Users(UserMixin, db.Model):
    __tablename__ = 'users'

    user_id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(200), nullable=False, unique=True)
    first_name = db.Column(db.String(30), nullable=False)
    last_name = db.Column(db.String(30), nullable=False)
    pass_hashed = db.Column(db.String, nullable=False)
    profile_path = db.Column(db.String, nullable=True)
    pitches = db.relationship('Pitches', backref='user', lazy='dynamic')
    comments = db.relationship('Comments', backref='user', lazy='dynamic')
    reactions = db.relationship('Reactions', backref='user', lazy='dynamic')

    def __repr__(self):
        return f'User -> {self.email}'

    @property
    def password(self):
        return AttributeError('Password cannot be red')

    @password.setter
    def password(self, password):
        self.pass_hashed = generate_password_hash(password, method='sha256', salt_length=8)

    def verify_password(self, password):
        return check_password_hash(self.pass_hashed, password)

    def get_id(self):
        return self.user_id


@login_manager.user_loader
def load_user(user_id):
    try:
        return Users.query.get(int(user_id))
    except:
        return None


class Pitches(db.Model):
    __tablename__ = 'pitches'

    pitch_id = db.Column(db.Integer, primary_key=True)
    pitch_content = db.Column(db.String, nullable=False)
    posted_on = db.Column(db.DateTime, default=datetime.utcnow)
    category_id = db.Column(db.Integer, db.ForeignKey('categories.category_id'))
    user_id = db.Column(db.Integer, db.ForeignKey('users.user_id'))
    comments = db.relationship('Comments', backref='pitch', lazy='dynamic')
    reactions = db.relationship('Reactions', backref='pitch', lazy='dynamic')

    def save_pitch(self):
        db.session.add(self)
        db.session.commit()

    @classmethod
    def get_pitches(cls, user_id):
        pitches = Pitches.query.filter_by(user_id=user_id).all()
        return pitches

    def get_likes(self, pitch_id):

        all_likes = []

        pitch = Pitches.query.filter_by(pitch_id=pitch_id).first()
        for reaction in pitch.reactions:
            if reaction.reaction == 1:
                all_likes.append(reaction)

        return len(all_likes)

    def get_dislikes(self, pitch_id):

        all_dislikes = []

        pitch = Pitches.query.filter_by(pitch_id=pitch_id).first()
        for reaction in pitch.reactions:
            if reaction.reaction == 0:
                all_dislikes.append(reaction)

        return len(all_dislikes)

    def get_author(self, pitch_id):
        author = Pitches.query.filter_by(pitch_id=pitch_id).first()
        print(author)
        return author


class Categories(db.Model):
    __tablename__ = 'categories'

    category_id = db.Column(db.Integer, primary_key=True)
    category_name = db.Column(db.String, unique=True, nullable=False)
    pitches = db.relationship('Pitches', backref='category', lazy='dynamic')

    def __repr__(self):
        return self.category_name


class Comments(db.Model):
    __tablename__ = 'comments'

    comment_id = db.Column(db.Integer, primary_key=True)
    comment = db.Column(db.String, nullable=False)
    posted_on = db.Column(db.DateTime, default=datetime.utcnow)
    pitch_id = db.Column(db.Integer, db.ForeignKey('pitches.pitch_id'))
    user_id = db.Column(db.Integer, db.ForeignKey('users.user_id'))

    def save_comment(self):
        db.session.add(self)
        db.session.commit()

    @classmethod
    def get_comment(cls, id):
        comments = Comments.query.filter_by(pitch_id=id).all()
        return comments


class Reactions(db.Model):
    __tablename__ = 'reactions'

    reaction_id = db.Column(db.Integer, primary_key=True)
    reaction = db.Column(db.Integer, nullable=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.user_id'))
    pitch_id = db.Column(db.Integer, db.ForeignKey('pitches.pitch_id'))

    def save_reaction(self):
        db.session.add(self)
        db.session.commit()

    @classmethod
    def get_reactions(cls, id):
        reactions = Reactions.query.filter_by(pitch_id=id).all()
        return reactions
