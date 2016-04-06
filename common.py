from basil import app, sql, db
from flask import session
from user.models import User, Following
from gardenDiary.models import Feed



def getFeedData(userID):

    followingList = []
    followingList.append(session['userID'])
    following = Following.query.filter_by(active=True).filter_by(user_id=session['userID']).all()
    for follower in following:
        followingList.append(follower.following_id)

    feed = Feed.query.filter_by(active=True)\
        .filter(Feed.user_id.in_(followingList))\
        .order_by(Feed.publish_date.desc())\
        .all()

    print "Qty-Feed: ", len(feed)

    return (feed)