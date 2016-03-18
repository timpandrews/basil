from flask_wtf import Form
from wtforms import validators, StringField, TextAreaField

class DiaryForm(Form):
    title = StringField('Title', validators=[
        validators.Required(),
        validators.Length(max=80)
        ])
    body = TextAreaField('Content', validators=[validators.Required()])
