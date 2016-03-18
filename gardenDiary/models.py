from basil import db
from datetime import datetime

class Diary(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    title = db.Column(db.String(80))
    body = db.Column(db.Text)
    publish_date = db.Column(db.DateTime)
    update_date = db.Column(db.DateTime)
    active = db.Column(db.Boolean)

    def __init__(self, user, title, body, publish_date=None, update_date=None, active=True):
        self.user_id = user.id
        self.title = title
        self.body = body
        if publish_date is None:
            self.publish_date = datetime.utcnow()
        else:
            self.publish_date = publish_date
        if update_date is None:
            self.update_date = datetime.utcnow()
        else:
            self.update_date = update_date
        self.active = active

    def __repr__(self):
        return '<diaryEntry %r>' % self.title