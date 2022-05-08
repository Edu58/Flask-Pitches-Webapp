from app import db
from datetime import datetime
from werkzeug.security import generate_password_hash, check_password_hash


class Users(db.Model):
    __tablename__ = 'users'

    user_id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(200), nullable=False, unique=True)
    first_name = db.Column(db.String(30), nullable=False)
    last_name = db.Column(db.String(30), nullable=False)
    pass_hashed = db.Column(db.String, nullable=False)
    profile_path = db.Column(db.String, nullable=False)
    pitches = db.relationship('Pitches', backref='user', lazy='dynamic')
    comments = db.relationship('Comments', backref='user', lazy='dynamic')
    reactions = db.relationship('Reactions', backref='user', lazy='dynamic')

    def __repr__(self):
        return f'User -> {self.first_name}, {self.last_name}, {self.pass_hashed}'

    @property
    def password(self):
        return AttributeError('Password cannot be red')

    @password.setter
    def password(self, password):
        self.pass_hashed = generate_password_hash(password, method='sha256', salt_length=8)

    def verify_password(self, password):
        return check_password_hash(self.pass_hashed, password)


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
    def get_pitches(cls, id):
        pitches = Pitches.query.filter_by(user_id=id).all()
        return pitches


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
