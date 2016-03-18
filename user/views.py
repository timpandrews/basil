from basil import app, sql, db
from flask import render_template, redirect, url_for, session, request
from user.forms import SignupForm, LoginForm
from user.models import User
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
                return redirect(url_for('login_success'))

        else: # bad username or password
            error = "Incorrect username and/or password"
            app.logger.warning('%s: Incorrect username and/or password: username:%s password:%s', datetime.datetime.utcnow(), form.username.data, form.password.data)

    return render_template('user/login.html', form=form, error=error)

@app.route('/signup', methods=('GET','POST'))
def signup():
    form = SignupForm()
    error = ""
    if form.validate_on_submit():
        # qry = """INSERT INTO user(fullname, email, username, password)
        #           VALUE (%s, %s, %s, %s)"""
        # print qry
        # cursor = sql.connect()
        # cursor.execute(qry, [form.fullname.data, form.fullname.data, form.username.data, form.password.data])
        # cursor.close

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
    session.pop('username')
    session.pop('userID')
    return redirect(url_for('index'))
