from basil import app, sql, db
from flask import render_template, redirect, url_for, session, request
from user.forms import SignupForm, LoginForm
from user.models import User
from gardenDiary.models import Diary
from user.decorators import login_required
import datetime

@app.route('/login', methods=('GET','POST'))
def login():
    form = LoginForm()
    error = None

    # Keeps track of requested url if redirected to login from another page
    if request.method == 'GET' and request.args.get('next'):
        session['next'] = request.args.get('next', None)

    if form.validate_on_submit():
        user = User.query.filter_by(
            username=form.username.data,
            password=form.password.data
            ).first()

        if user: # if user is found
            session['username'] = form.username.data
            session['userID'] = user.id

            # if they were redirect to login then send to original requested url
            if 'next' in session:
                next = session.get('next')
                session.pop('next')
                return redirect(next)
            else: # otherwise send to login_success page
                app.logger.info('%s: Successful login for: %s', datetime.datetime.utcnow(), form.username.data)

                diary = Diary.query.filter_by(active=True)\
                    .filter_by(user_id=session['userID'])\
                    .order_by(Diary.publish_date.desc())\
                    .paginate(1, app.config['POSTS_PER_PAGE'], False)
                return render_template('gardenDiary/dashboard.html', diary=diary)

        else: # bad username or password
            error = "Incorrect username and/or password"
            app.logger.warning('%s: Incorrect username and/or password: username:%s ', datetime.datetime.utcnow(), form.username.data)

    return render_template('user/login.html', form=form, error=error)

@app.route('/signup', methods=('GET','POST'))
def signup():
    form = SignupForm()
    error = ""
    if form.validate_on_submit():

        newUser = User(
            form.fullname.data,
            form.email.data,
            form.username.data,
            form.password.data
            )
        db.session.add(newUser)

        # Similar to triggers.  Runs all actions in session.  Builds new records & can return new id fields, but data is temporary until commit()
        # db.session.flush()
        # print "Trigger ID: ", newUser.id

        db.session.commit()
        app.logger.info('%s: New User Signup:%s ', datetime.datetime.utcnow(), form.username.data)


        return redirect(url_for('welcome'))
    return render_template('user/signup.html', form=form, username=form.username.data)

# New User Welcome Page
@app.route('/welcome')
def welcome():
    return render_template('user/welcome.html')


@app.route('/login_success')
# @login_required
def login_success():
    return render_template('user/login_success.html', username=session['username'])

@app.route('/logout')
def logout():
    app.logger.info('%s: User Logged Out: %s', datetime.datetime.utcnow(), session.get('username'))
    session.pop('username')
    session.pop('userID')
    return redirect(url_for('index'))
