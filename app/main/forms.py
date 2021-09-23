from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, IntegerField, TextAreaField
from wtforms import validators
from wtforms.fields.core import RadioField
from wtforms.validators import Required

class PitchForm(FlaskForm):

    pitchtitle = StringField('Pitch title', validators=[Required()])
    mypitch = TextAreaField('Pitch', validators=[Required()])
    author = StringField('Author : ', validators=[Required()])
    category = RadioField('Pitch Category', choices=[('pickup lines', 'pickup lines'), ('interview pitch', 'interview pitch'), ('product pitch', 'product pitch'), ('promotion pitch', 'promotion pitch')])
    submit = SubmitField('Submit')