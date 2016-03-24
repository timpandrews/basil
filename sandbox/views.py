from basil import app, sql, db
from flask import render_template, redirect, url_for, session, request
# from sandbox.models import sb_Bookmark, sb_User


@app.route('/sandbox')
def sandbox():
    return "sandbox"