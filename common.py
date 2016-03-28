from basil import app, sql, db
from flask import session
from user.models import User, Following
from gardenDiary.models import Diary

def getDiary(userID,page):

    followingList = []
    followingList.append(session['userID'])
    following = Following.query.filter_by(active=True).filter_by(user_id=session['userID']).all()
    for follower in following:
        followingList.append(follower.following_id)

    diary = Diary.query.filter_by(active=True)\
        .filter(Diary.user_id.in_(followingList))\
        .order_by(Diary.publish_date.desc())\
        .paginate(page, app.config['POSTS_PER_PAGE'], False)

    return diary