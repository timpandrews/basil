from basil import db, uploaded_images
from datetime import datetime

class Feed(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    feedType = db.Column(db.String(3))
    title = db.Column(db.String(80))
    detail = db.Column(db.Text)
    reminderStartDate = db.Column(db.DateTime)
    reminderEndDate = db.Column(db.DateTime)
    plantingType = db.Column(db.String(4))
    plantingDate = db.Column(db.DateTime)
    plantName = db.Column(db.String(256))
    badge = db.Column(db.String(256))
    displayDate = db.Column(db.DateTime)
    publish_date = db.Column(db.DateTime)
    update_date = db.Column(db.DateTime)
    public = db.Column(db.Boolean)
    active = db.Column(db.Boolean)

    diaryUser = db.relationship('User', backref='diary', lazy='joined', uselist=False)

    @property
    def imgsrc(self):
        return uploaded_images.url(self.badge)

    def __init__(self,
                 user,
                 feedType,
                 title,
                 detail,
                 reminderStartDate,
                 reminderEndDate,
                 plantingType,
                 plantingDate,
                 plantName,
                 displayDate,
                 badge=None,
                 publish_date=None,
                 update_date=None,
                 public=True,
                 active=True):
        self.user_id = user.id
        self.feedType =feedType
        self.title = title
        self.detail = detail
        self.badge = badge
        self.reminderStartDate = reminderStartDate
        self.reminderEndDate = reminderEndDate
        self.plantingType = plantingType
        self.plantingDate = plantingDate
        self.plantName = plantName
        self.displayDate = displayDate
        if publish_date is None:
            self.publish_date = datetime.utcnow()
        else:
            self.publish_date = publish_date
        if update_date is None:
            self.update_date = datetime.utcnow()
        else:
            self.update_date = update_date
        self.public = public
        self.active = active

    def __repr__(self):
        return '<FeedEntry %r>' % self.title





