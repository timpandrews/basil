from basil import db
from datetime import datetime

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    fullname = db.Column(db.String(80))
    email = db.Column(db.String(35)) # email = db.Column(db.String(35), unique=True)
    username = db.Column(db.String(80)) # username = db.Column(db.String(80), unique=True)
    password = db.Column(db.String(60))
    active = db.Column(db.Boolean)

    def __init__(self, fullname, email, username, password, active=True):
        self.fullname = fullname
        self.email = email
        self.username = username
        self.password = password
        self.active = active

    def __repr__(self):
        return '<User %r>' % self.username

class Following(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    following_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    create_date = db.Column(db.DateTime)
    active = db.Column(db.Boolean)

    followingUser = db.relationship('User', foreign_keys=[following_id], backref='Following', lazy='joined', uselist=False)

    def __init__(self, user_id, following_id, create_date=None, active=True):
        self.user_id = user_id
        self.following_id = following_id
        if create_date is None:
            self.create_date = datetime.utcnow()
        else:
            self.create_date = create_date
        self.active = active

    def __repr__(self):
        return  '<Following %r>' % self.user_id, self.followingUser
