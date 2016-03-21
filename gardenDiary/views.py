from basil import app, db
from flask import render_template, redirect, url_for, session, request
from gardenDiary.forms import DiaryForm
from gardenDiary.models import Diary
from user.models import User
from user.decorators import login_required
import datetime

POSTS_PER_PAGE = 5

@app.route('/')
@app.route('/index')
def index():
    return render_template('home.html')

@app.route('/dashboard') #aka Garden Diary
@login_required
def dashboard():
    diary = Diary.query.filter_by(active=True).order_by(Diary.publish_date.desc())
    return render_template('gardenDiary/dashboard.html', diary=diary)

@app.route('/gardenDiaryEntry', methods=('GET', 'POST')) # Add New &?? Edit??
@login_required
def gardenDiaryEntry():
    form = DiaryForm()

    if form.validate_on_submit():
        user = User.query.filter_by(id=session['userID']).first()
        title = form.title.data
        body = form.body.data
        diaryEntry = Diary(user, title, body)
        db.session.add(diaryEntry)
        db.session.commit()
        app.logger.info('%s: New Diary Entry: %s by: %s', datetime.datetime.utcnow(), form.title.data, session.get('username'))

        diary = Diary.query.filter_by(active=True).order_by(Diary.publish_date.desc())
        return render_template('gardenDiary/dashboard.html', diary=diary)

    return render_template('gardenDiary/gardenDiaryEntry.html', form=form, action="new")

@app.route('/gardenDiaryEntryDetail/<int:diary_id>')
@login_required
def gardenDiaryEntryDetail(diary_id):
    entry = Diary.query.filter_by(id=diary_id).first_or_404()
    return render_template('gardenDiary/gardenDiaryEntryDetail.html', entry=entry)

@app.route('/delete/<int:diary_id>')
@login_required
def delete(diary_id):
    entry = Diary.query.filter_by(id=diary_id).first_or_404()
    entry.active = False
    db.session.commit()
    app.logger.info('%s: Deleted Diary Entry: %s by: %s', datetime.datetime.utcnow(), entry.title, session.get('username'))
    # flash("entry deleted")

    diary = Diary.query.filter_by(active=True).order_by(Diary.publish_date.desc())
    return render_template('gardenDiary/dashboard.html', diary=diary)