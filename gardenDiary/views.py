from basil import app
from flask import render_template, redirect, url_for, session, request
from user.forms import SignupForm
from user.decorators import login_required


@app.route('/')
@app.route('/index')
def index():
    return render_template('home.html')

@app.route('/dashboard') #aka Garden Diary
@login_required
def dashboard():
    return render_template('gardenDiary/dashboard.html')

@app.route('/gardenDiaryEntry') # Add New &?? Edit??
@login_required
def gardenDiaryEntry():
    return render_template('gardenDiary/gardenDiaryEntry.html')