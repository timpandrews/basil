from basil import app, sql, db
from flask import session
from user.models import User, Following
from gardenDiary.models import Diary, Reminder, Planting

def getDiary(userID):

    followingList = []
    followingList.append(session['userID'])
    following = Following.query.filter_by(active=True).filter_by(user_id=session['userID']).all()
    for follower in following:
        followingList.append(follower.following_id)

    diary = Diary.query.filter_by(active=True)\
        .filter(Diary.user_id.in_(followingList))\
        .order_by(Diary.publish_date.desc())\
        .all()

    return diary

def getReminders(userID):

    reminders = Reminder.query.filter_by(active=True)\
        .filter_by(user_id=userID)\
        .order_by(Reminder.reminder_date.desc())\
        .all()

    return reminders


def getPlantings(userID):

    plantings = Planting.query.filter_by(active=True)\
        .filter_by(user_id=userID)\
        .order_by(Planting.publish_date.desc())\
        .all()

    return plantings