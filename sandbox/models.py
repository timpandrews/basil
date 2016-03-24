# from datetime import datetime
# from basil import db
#
# class sb_Bookmark(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     url = db.Column(db.Text, nullable=False)
#     date = db.Column(db.DateTime, default=datetime.utcnow)
#     description = db.Column(db.String(300))
#     # user_id = db.Column(db.Integer, db.ForeignKey('sb_user.id'), nullable=False)
#
#     def __repr__(self):
#         return "<sb_Bookmark '{}': '{}'>".format(self.description, self.url)
#
# class sb_User(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     username = db.Column(db.String(80), unique=True)
#     email = db.Column(db.String(300))
#     # bookmarks = db.relationship('sb_Bookmark', backref='sb_user', lazy='dynamic')
#
#     def __repr__(self):
#         return '<sb_User %r>' % self.username