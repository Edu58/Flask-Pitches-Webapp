from flask_wtf import FlaskForm
from wtforms import TextAreaField, SubmitField, SelectField
from wtforms.validators import DataRequired, length


class NewPitchForm(FlaskForm):
    category = SelectField('Choose Pitch Category', validators=[DataRequired()],
                           choices=[('interview', 'interview'), ('promotion', 'promotion'),
                                    ('product', 'product'),
                                    ('pickup line', 'pickup line')])
    pitch = TextAreaField('Pitch Content', validators=[DataRequired()])
    submit = SubmitField('submit')


class CommentForm(FlaskForm):
    comment = TextAreaField('Write Your Comment', validators=[DataRequired(), length(max=200)])
    submit = SubmitField('comment')
