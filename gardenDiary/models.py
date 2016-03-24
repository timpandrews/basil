from basil import db, uploaded_images
from datetime import datetime

class Diary(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    title = db.Column(db.String(80))
    body = db.Column(db.Text)
    badge = db.Column(db.String(256))
    publish_date = db.Column(db.DateTime)
    update_date = db.Column(db.DateTime)
    active = db.Column(db.Boolean)
    diaryUser = db.relationship('User', backref='diary', lazy='joined', uselist=False)

    @property
    def imgsrc(self):
        return uploaded_images.url(self.badge)

    def __init__(self, user, title, body, badge=None, publish_date=None, update_date=None, active=True):
        self.user_id = user.id
        self.title = title
        self.body = body
        self.badge = badge
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