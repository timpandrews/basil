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
        self.plantName = plantName
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

class Reminder(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    title = db.Column(db.String(80))
    detail = db.Column(db.Text)
    badge = db.Column(db.String(256))
    reminder_date = db.Column(db.DateTime)
    create_date = db.Column(db.DateTime)
    update_date = db.Column(db.DateTime)
    active = db.Column(db.Boolean)

    @property
    def imgsrc(self):
        return uploaded_images.url(self.badge)

    def __init__(self, user, title, detail, reminder_date, badge=None, create_date=None, update_date=None, active=True):
        self.user_id = user.id
        self.title = title
        self.detail = detail
        self.reminder_date = reminder_date
        self.badge = badge
        if create_date is None:
            self.create_date = datetime.utcnow()
        else:
            self.publish_date = publish_date
        if update_date is None:
            self.update_date = datetime.utcnow()
        else:
            self.update_date = update_date
        self.active = active

    def __repr__(self):
        return '<reminder %r>' % self.title

class Planting(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    plantingType = db.Column(db.String(75))
    plantName = db.Column(db.String(256))
    badge = db.Column(db.String(256))
    publish_date = db.Column(db.DateTime)
    update_date = db.Column(db.DateTime)
    active = db.Column(db.Boolean)

    @property
    def imgsrc(self):
        return uploaded_images.url(self.badge)

    def __init__(self, user, plantingType, plantName, badge=None, publish_date=None, update_date=None, active=True):
        self.user_id = user.id
        self.plantingType = plantingType
        self.plantName = plantName
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
        return '<planting %r>' % self.plantName

