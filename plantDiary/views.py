from basil import app
from flask import render_template, redirect

@app.route('/')
@app.route('/index')
def index():
    return render_template('home.html')