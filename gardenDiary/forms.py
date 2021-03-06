from flask_wtf import Form
from wtforms import validators, StringField, TextAreaField, DateField, SelectField
from flask_wtf.file import FileField, FileAllowed
import datetime

class DiaryForm(Form):
    badge = FileField('Badge', validators=[
        FileAllowed(['jpg', 'jpeg', 'png'], 'Images only.')
        ])
    title = StringField('Title', validators=[
        validators.Required(),
        validators.Length(max=80)
        ])
    detail = TextAreaField('Content', validators=[validators.Required()])
    displayDate = DateField(
        'Diary Entry Date',
        format='%m/%d/%Y',
        default=datetime.date.today,
        validators=[validators.Required()]
        )

class ReminderForm(Form):
    badge = FileField('Badge', validators=[
        FileAllowed(['jpg', 'jpeg', 'png'], 'Images only.')
        ])
    title = StringField('Title', validators=[
        validators.Required(),
        validators.Length(max=80)
        ])
    detail = TextAreaField('Detail', validators=[validators.Required()])
    reminderStartDate = DateField('Reminder Date', format='%m/%d/%Y', validators=[validators.Required()])

class PlantingForm(Form):
    badge = FileField('Badge', validators=[
        FileAllowed(['jpg', 'jpeg', 'png'], 'Images only.')
        ])
    plantName = StringField('Plant Name', validators=[
        validators.Required(),
        validators.Length(max=256)
        ])
    plantingType = SelectField(
        'Planting Type',
        choices=[('sowI', 'Sow seeds indoor'), ('sowO', 'Sow seeds outdoors'), ('tran', 'Transplant seedlings outdoors')]
        )
    plantingDate = DateField(
        'Planting Date',
        format='%m/%d/%Y',
        default=datetime.date.today,
        validators=[validators.Required()]
        )