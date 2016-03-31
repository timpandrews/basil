from basil import app, db, uploaded_images
from flask import render_template, redirect, url_for, session, request, flash, jsonify
from gardenDiary.forms import DiaryForm, ReminderForm
from gardenDiary.models import Diary, Reminder
from user.models import User, Following
from user.decorators import login_required
import datetime
from common import getDiary


@app.route('/')
@app.route('/index')
def index():
    return render_template('home.html')

@app.route('/dashboard') #aka Garden Diary
@app.route('/dashboard/<int:page>')
@login_required
#dahsbooard
def dashboard(page=1):

    diary = getDiary(session['userID'],page)

    return render_template('gardenDiary/dashboard.html', diary=diary)

@app.route('/entry', methods=('GET', 'POST')) # Add New
@login_required
#dashboard
def entry():
    form = DiaryForm()

    if form.validate_on_submit():
        badge = request.files.get('badge')
        filename = None
        try:
            filename = uploaded_images.save(badge)
        except:
            flash("The image was not uploaded")
        user = User.query.filter_by(id=session['userID']).first()
        title = form.title.data
        body = form.body.data
        diaryEntry = Diary(user, title, body, filename)
        db.session.add(diaryEntry)
        db.session.commit()
        flash("New Diary Entry Saved!")
        app.logger.info('%s: New Diary Entry: %s by: %s', datetime.datetime.utcnow(), form.title.data, session.get('username'))

        diary = getDiary(session['userID'],1)

        return render_template('gardenDiary/dashboard.html', diary=diary)

    return render_template('gardenDiary/entry.html', form=form, action="new")

@app.route('/entryDetail/<int:diary_id>')
@login_required
def entryDetail(diary_id):
    entry = Diary.query.filter_by(id=diary_id).first_or_404()
    return render_template('gardenDiary/entryDetail.html', entry=entry)

@app.route('/delete/<int:diary_id>')
@login_required
#dashboard
def delete(diary_id):
    entry = Diary.query.filter_by(id=diary_id).first_or_404()
    entry.active = False
    db.session.commit()
    flash("Diary Entry Deleted")
    app.logger.info('%s: Deleted Diary Entry: %s by: %s', datetime.datetime.utcnow(), entry.title, session.get('username'))

    diary = getDiary(session['userID'],1)

    return render_template('gardenDiary/dashboard.html', diary=diary)

@app.route('/edit/<int:diary_id>', methods=('GET', 'POST'))
@login_required
def edit(diary_id):
    entry = Diary.query.filter_by(id=diary_id).first_or_404()
    form = DiaryForm(obj=entry)
    if form.validate_on_submit():
        original_badge = entry.badge
        form.populate_obj(entry) # replaced entry with new data from form.
        print "entry.badge: ", entry.badge
        print "form.badge.has_file(): ", form.badge.has_file()
        if form.badge.has_file():
            badge = request.files.get('badge')
            print "badge: ", badge
            try:
                filename = uploaded_images.save(badge)
            except:
                flash("The image was not uploaded")
            if filename:
                entry.badge = filename
        else:
            entry.badge = original_badge

        db.session.commit()
        flash("Diary Entry Updated!")
        app.logger.info('%s: Updated Diary Entry: %s by: %s', datetime.datetime.utcnow(), entry.title, session.get('username'))
        return redirect(url_for('entryDetail', diary_id=diary_id))
    return render_template('gardenDiary/entry.html', form=form, entry=entry, action="edit")

@app.route('/gardeners')
@login_required
def gardeners():
    following = Following.query.filter_by(active=True).filter_by(user_id=session['userID']).all()
    suggestedGardeners = User.query.filter_by(active=True).filter(User.id != session['userID']).all()

    # Build isFollowingList -Checks suggestedGarderns List against following list
    # to find matches creats ordered list of restuls
    isFollowingList = []
    for gardeners in suggestedGardeners:
        isFollowing = False
        for followed in following:
            if gardeners.id == followed.following_id:
                isFollowing = True
        isFollowingList.append(isFollowing)

    return render_template('gardenDiary/gardeners.html', following=following, suggestedGardeners=suggestedGardeners, isFollowingList=isFollowingList)

# Currently following change to not following
@app.route('/toggleFollowing')
def toggleFollowing():
    button_id = request.args.get('id')
    gardener_id = button_id.split("_",1)[1] # Strip of prefix & return just id:int

    # set active=false for record from tbl: following
    removeFollow = Following.query.filter_by(user_id=session.get('userID')).filter_by(following_id=gardener_id).first_or_404()
    removeFollow.active = False
    db.session.commit()
    app.logger.info('%s: Remove Following by: %s', datetime.datetime.utcnow(), session.get('username'))

    return jsonify(button_id=button_id)

# Currently not following change to following
@app.route('/toggleNotFollowing')
def toggleNotFollowing():
    button_id = request.args.get('id')
    gardener_id = button_id.split("_",1)[1] # Strip of prefix & return just id:int

    # add or update record to tbl: following
    if Following.query.filter_by(user_id=session.get('userID')).filter_by(following_id=gardener_id).count():
        # found existing record, update existing record with active = true
        follow = Following.query.filter_by(user_id=session.get('userID')).filter_by(following_id=gardener_id).first()
        follow.active = True
        db.session.commit()
    else:
        # no record found, add new record
        newFollow = Following(session.get('userID'),gardener_id)
        db.session.add(newFollow)
        db.session.commit()

    app.logger.info('%s: New Following by: %s', datetime.datetime.utcnow(), session.get('username'))




    return jsonify(button_id=button_id)

@app.route('/reminder', methods=('GET', 'POST'))
@login_required
def reminder():
    form = ReminderForm()

    if form.validate_on_submit():
        badge = request.files.get('badge')
        filename = None
        try:
            filename = uploaded_images.save(badge)
        except:
            flash("The image was not uploaded")
        user = User.query.filter_by(id=session['userID']).first()
        title = form.title.data
        detail = form.detail.data
        reminder = Reminder(user, title, detail, filename)
        db.session.add(reminder)
        db.session.commit()
        flash("New Reminder Created!")
        app.logger.info('%s: New New Reminder: %s by: %s', datetime.datetime.utcnow(), form.title.data, session.get('username'))

        diary = getDiary(session['userID'],1)

        return render_template('gardenDiary/dashboard.html', diary=diary)

    return render_template('gardenDiary/reminder.html', form=form, action="new")