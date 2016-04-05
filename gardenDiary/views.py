from basil import app, db, uploaded_images
from flask import render_template, redirect, url_for, session, request, flash, jsonify
from gardenDiary.forms import DiaryForm, ReminderForm, PlantingForm
from gardenDiary.models import Diary, Reminder, Planting
from user.models import User, Following
from user.decorators import login_required
import datetime
from common import getDiary, getReminders, getPlantings

### Index/Home Page ###
@app.route('/')
@app.route('/index')
def index():
    return render_template('home.html')


### Dashboard Page ###
@app.route('/dashboard') #aka Garden Diary
@app.route('/dashboard/<int:page>')
@login_required
#dashboard
def dashboard(page=None):
    records_per_page = app.config['DEFAULT_ENTRIES_PER_PAGE']
    if not page:
        show_records = app.config['DEFAULT_ENTRIES_PER_PAGE']
    else:
        show_records = page
    diary = getDiary(session['userID'])
    reminders = getReminders(session['userID'])
    plantings = getPlantings(session['userID'])
    return render_template('gardenDiary/dashboard.html', diary=diary, reminders=reminders, plantings=plantings, show_records=show_records, records_per_page=records_per_page)


### Diary Entry Add/Edit/Delete Pages ###
@app.route('/entry', methods=('GET', 'POST')) # Add New
@login_required
#dashboard
def diaryEntry():
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

        records_per_page = app.config['DEFAULT_ENTRIES_PER_PAGE']
        show_records = app.config['DEFAULT_ENTRIES_PER_PAGE']
        diary = getDiary(session['userID'])
        reminders = getReminders(session['userID'])
        return render_template('gardenDiary/dashboard.html', diary=diary, reminders=reminders, show_records=show_records, records_per_page=records_per_page)

    return render_template('gardenDiary/diaryEntry.html', form=form, action="new")

@app.route('/entryDetail/<int:diary_id>')
@login_required
def diaryEntryDetail(diary_id):
    entry = Diary.query.filter_by(id=diary_id).first_or_404()
    return render_template('gardenDiary/diaryEntryDetail.html', entry=entry)

@app.route('/delete/<int:diary_id>')
@login_required
#dashboard
def diaryEntryDelete(diary_id):
    entry = Diary.query.filter_by(id=diary_id).first_or_404()
    entry.active = False
    db.session.commit()
    flash("Diary Entry Deleted")
    app.logger.info('%s: Deleted Diary Entry: %s by: %s', datetime.datetime.utcnow(), entry.title, session.get('username'))

    records_per_page = app.config['DEFAULT_ENTRIES_PER_PAGE']
    show_records = app.config['DEFAULT_ENTRIES_PER_PAGE']
    diary = getDiary(session['userID'])
    reminders = getReminders(session['userID'])
    return render_template('gardenDiary/dashboard.html', diary=diary, reminders=reminders, show_records=show_records, records_per_page=records_per_page)

@app.route('/edit/<int:diary_id>', methods=('GET', 'POST'))
@login_required
def diaryEntryEdit(diary_id):
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
        return redirect(url_for('diaryEntryDetail', diary_id=diary_id))
    return render_template('gardenDiary/diaryEntry.html', form=form, entry=entry, action="edit")

### New Plantings Add/Edit/Delete Pages ###
@app.route('/planting', methods=('GET', 'POST'))
@login_required
def planting():
    form = PlantingForm()

    if form.validate_on_submit():
        badge = request.files.get('badge')
        filename = None
        try:
            filename = uploaded_images.save(badge)
        except:
            flash("The image was not uploaded")
        user = User.query.filter_by(id=session['userID']).first()
        plantingType = form.plantingType.data
        plantName = form.plantName.data
        planting = Planting(user, plantingType, plantName, filename)
        db.session.add(planting)
        db.session.commit()
        flash("New Planting Created!")
        app.logger.info('%s: New Planting: %s by: %s', datetime.datetime.utcnow(), form.plantName.data, session.get('username'))

        records_per_page = app.config['DEFAULT_ENTRIES_PER_PAGE']
        show_records = app.config['DEFAULT_ENTRIES_PER_PAGE']
        diary = getDiary(session['userID'])
        reminders = getReminders(session['userID'])
        return render_template('gardenDiary/dashboard.html', diary=diary, reminders=reminders, show_records=show_records, records_per_page=records_per_page)

    return render_template('gardenDiary/planting.html', form=form, action="new")

@app.route('/plantingDetail/<int:planting_id>')
@login_required
def plantingDetail(planting_id):
    planting = Planting.query.filter_by(id=planting_id).first_or_404()
    return render_template('gardenDiary/plantingDetail.html', planting=planting)

@app.route('/plantingDelete/<int:planting_id>')
@login_required
#dashboard
def plantingDelete(planting_id):
    planting = Planting.query.filter_by(id=planting_id).first_or_404()
    planting.active = False
    db.session.commit()
    flash("Planting Deleted")
    app.logger.info('%s: Deleted planting: %s by: %s', datetime.datetime.utcnow(), planting.plantName, session.get('username'))

    records_per_page = app.config['DEFAULT_ENTRIES_PER_PAGE']
    show_records = app.config['DEFAULT_ENTRIES_PER_PAGE']
    diary = getDiary(session['userID'])
    reminders = getReminders(session['userID'])
    plantings = getPlantings(session['userID'])
    return render_template('gardenDiary/dashboard.html', diary=diary, reminders=reminders, plantings=plantings, show_records=show_records, records_per_page=records_per_page)

@app.route('/plantingEdit/<int:planting_id>', methods=('GET', 'POST'))
@login_required
def plantingEdit(planting_id):
    planting = Planting.query.filter_by(id=planting_id).first_or_404()
    form = PlantingForm(obj=planting)
    if form.validate_on_submit():
        original_badge = planting.badge
        form.populate_obj(planting) # replaced entry with new data from form.
        if form.badge.has_file():
            badge = request.files.get('badge')
            try:
                filename = uploaded_images.save(badge)
            except:
                flash("The image was not uploaded")
            if filename:
                planting.badge = filename
        else:
            planting.badge = original_badge

        db.session.commit()
        flash("Planting Updated!")
        app.logger.info('%s: Upldated Planting: %s by: %s', datetime.datetime.utcnow(), planting.plantName, session.get('username'))
        return redirect(url_for('plantingDetail', planting_id=planting_id))
    return render_template('gardenDiary/planting.html', form=form, planting=planting, action="edit")


### Reminder Add/Edit/Delete Pages ###
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
        reminder_date = form.reminder_date.data
        reminder = Reminder(user, title, detail, reminder_date, filename)
        db.session.add(reminder)
        db.session.commit()
        flash("New Reminder Created!")
        app.logger.info('%s: New New Reminder: %s by: %s', datetime.datetime.utcnow(), form.title.data, session.get('username'))

        records_per_page = app.config['DEFAULT_ENTRIES_PER_PAGE']
        show_records = app.config['DEFAULT_ENTRIES_PER_PAGE']
        diary = getDiary(session['userID'])
        reminders = getReminders(session['userID'])
        return render_template('gardenDiary/dashboard.html', diary=diary, reminders=reminders, show_records=show_records, records_per_page=records_per_page)

    return render_template('gardenDiary/reminder.html', form=form, action="new")

@app.route('/reminderDetail/<int:reminder_id>')
@login_required
def reminderDetail(reminder_id):
    reminder = Reminder.query.filter_by(id=reminder_id).first_or_404()
    return render_template('gardenDiary/reminderDetail.html', reminder=reminder)

@app.route('/reminderDelete/<int:reminder_id>')
@login_required
#dashboard
def reminderDelete(reminder_id):
    reminder = Reminder.query.filter_by(id=reminder_id).first_or_404()
    reminder.active = False
    db.session.commit()
    flash("Reminder Deleted")
    app.logger.info('%s: Deleted Reminder: %s by: %s', datetime.datetime.utcnow(), reminder.title, session.get('username'))

    records_per_page = app.config['DEFAULT_ENTRIES_PER_PAGE']
    show_records = app.config['DEFAULT_ENTRIES_PER_PAGE']
    diary = getDiary(session['userID'])
    reminders = getReminders(session['userID'])
    return render_template('gardenDiary/dashboard.html', diary=diary, reminders=reminders, show_records=show_records, records_per_page=records_per_page)

@app.route('/reminderEdit/<int:reminder_id>', methods=('GET', 'POST'))
@login_required
def reminderEdit(reminder_id):
    reminder = Reminder.query.filter_by(id=reminder_id).first_or_404()
    form = ReminderForm(obj=reminder)
    if form.validate_on_submit():
        original_badge = reminder.badge
        form.populate_obj(reminder) # replaced entry with new data from form.
        if form.badge.has_file():
            badge = request.files.get('badge')
            try:
                filename = uploaded_images.save(badge)
            except:
                flash("The image was not uploaded")
            if filename:
                reminder.badge = filename
        else:
            reminder.badge = original_badge

        db.session.commit()
        flash("Reminder Updated!")
        app.logger.info('%s: Updated Reminder: %s by: %s', datetime.datetime.utcnow(), reminder.title, session.get('username'))
        return redirect(url_for('reminderDetail', reminder_id=reminder_id))
    return render_template('gardenDiary/reminder.html', form=form, reminder=reminder, action="edit")

### Gardeners Page ###
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

