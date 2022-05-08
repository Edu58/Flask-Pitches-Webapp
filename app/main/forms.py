from flask_wtf import FlaskForm
from wtforms import TextAreaField, SubmitField, SelectField
from wtforms.validators import DataRequired


class NewPitchForm(FlaskForm):
    category = SelectField('Pitch Category', validators=[DataRequired()],
                           choices=['interview', 'product', 'promotion', 'pickup line'])
    pitch = TextAreaField('Pitch Content', validators=[DataRequired()])
    submit = SubmitField('submit')
