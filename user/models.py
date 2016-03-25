from basil import db

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
    followingUser = db.relationship('User', foreign_keys=[following_id], backref='Following', lazy='joined', uselist=False)
