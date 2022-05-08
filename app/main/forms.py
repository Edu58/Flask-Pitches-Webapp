from flask_wtf import FlaskForm
from wtforms import TextAreaField, SubmitField, SelectField
from wtforms.validators import DataRequired
from ..models import Categories


class NewPitchForm(FlaskForm):
    category = SelectField('Choose Pitch Category', validators=[DataRequired()],
                           choices=[('interview', 'interview'), ('product', 'product'),
                                    ('promotion', 'promotion'),
                                    ('pickup-line', 'pickup line')])
    pitch = TextAreaField('Pitch Content', validators=[DataRequired()])
    submit = SubmitField('submit')
