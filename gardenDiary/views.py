from basil import app, db
from flask import render_template, redirect, url_for, session, request, flash
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
    diary = Diary.query.filter_by(active=True).filter_by(user_id=session['userID']).order_by(Diary.publish_date.desc())
    return render_template('gardenDiary/dashboard.html', diary=diary)

@app.route('/entry', methods=('GET', 'POST')) # Add New
@login_required
def entry():
    form = DiaryForm()

    if form.validate_on_submit():
        user = User.query.filter_by(id=session['userID']).first()
        title = form.title.data
        body = form.body.data
        diaryEntry = Diary(user, title, body)
        db.session.add(diaryEntry)
        db.session.commit()
        flash("New Diary Entry Saved!")
        app.logger.info('%s: New Diary Entry: %s by: %s', datetime.datetime.utcnow(), form.title.data, session.get('username'))

        diary = Diary.query.filter_by(active=True).filter_by(user_id=session['userID']).order_by(Diary.publish_date.desc())
        return render_template('gardenDiary/dashboard.html', diary=diary)

    return render_template('gardenDiary/entry.html', form=form, action="new")

@app.route('/entryDetail/<int:diary_id>')
@login_required
def entryDetail(diary_id):
    entry = Diary.query.filter_by(id=diary_id).first_or_404()
    return render_template('gardenDiary/entryDetail.html', entry=entry)

@app.route('/delete/<int:diary_id>')
@login_required
def delete(diary_id):
    entry = Diary.query.filter_by(id=diary_id).first_or_404()
    entry.active = False
    db.session.commit()
    flash("Diary Entry Deleted")
    app.logger.info('%s: Deleted Diary Entry: %s by: %s', datetime.datetime.utcnow(), entry.title, session.get('username'))
    # flash("entry deleted")

    diary = Diary.query.filter_by(active=True).filter_by(user_id=session['userID']).order_by(Diary.publish_date.desc())
    return render_template('gardenDiary/dashboard.html', diary=diary)

@app.route('/edit/<int:diary_id>', methods=('GET', 'POST'))
@login_required
def edit(diary_id):
    print diary_id
    entry = Diary.query.filter_by(id=diary_id).first_or_404()
    form = DiaryForm(obj=entry)
    if form.validate_on_submit():
        form.populate_obj(entry) # replaced entry with new data from form.
        db.session.commit()
        flash("Diary Entry Updated!")
        app.logger.info('%s: Updated Diary Entry: %s by: %s', datetime.datetime.utcnow(), entry.title, session.get('username'))
        return redirect(url_for('entryDetail', diary_id=diary_id))
    return render_template('gardenDiary/entry.html', form=form, entry=entry, action="edit")