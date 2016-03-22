from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy
from flask.ext.migrate import Migrate
from sqlalchemy import create_engine
from flask.ext.uploads import UploadSet, configure_uploads, IMAGES

app = Flask(__name__)
app.config.from_object('settings')
db = SQLAlchemy(app)

sql = create_engine(app.config['DB_URI'], pool_size=20, max_overflow=0, pool_recycle=300)

# logging
import logging
from logging.handlers import RotatingFileHandler
handler = RotatingFileHandler('event.log', maxBytes=10000, backupCount=1)
handler.setLevel(logging.INFO)
app.logger.addHandler(handler)


# Migrations
migrate = Migrate(app, db)


# flask-upload images
uploaded_images = UploadSet('images', IMAGES)
configure_uploads(app, uploaded_images)


from gardenDiary import views
from user import views