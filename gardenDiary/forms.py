from flask_wtf import Form
from wtforms import validators, StringField, TextAreaField
from flask_wtf.file import FileField, FileAllowed

class DiaryForm(Form):
    badge = FileField('Badge', validators=[
        FileAllowed(['jpg', 'png'], 'Images only.')
        ])
    title = StringField('Title', validators=[
        validators.Required(),
        validators.Length(max=80)
        ])
    body = TextAreaField('Content', validators=[validators.Required()])

class ReminderForm(Form):
    badge = FileField('Badge', validators=[
        FileAllowed(['jpg', 'png'], 'Images only.')
        ])
    title = StringField('Title', validators=[
        validators.Required(),
        validators.Length(max=80)
        ])
    detail = TextAreaField('Detail', validators=[validators.Required()])
