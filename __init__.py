from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy
from flask.ext.migrate import Migrate
from sqlalchemy import create_engine
from flask.ext.uploads import UploadSet, configure_uploads, IMAGES

app = Flask(__name__)
app.config.from_object('settings')
db = SQLAlchemy(app)

sql = create_engine(app.config['DB_URI'], pool_size=20, max_overflow=0, pool_recycle=300, echo=True)

# logging
import logging
from logging.handlers import RotatingFileHandler
handler = RotatingFileHandler('event.log', maxBytes=10000, backupCount=1)
handler.setLevel(logging.INFO)
app.logger.addHandler(handler)

# db loggin
db_handler_log_level = logging.INFO
db_logger_log_level = logging.INFO

# db_handler = logging.FileHandler('db.log')
db_handler = RotatingFileHandler('db.log', maxBytes=10000, backupCount=1)
db_handler.setLevel(db_handler_log_level)

db_logger = logging.getLogger('sqlalchemy')
db_logger.addHandler(db_handler)
db_logger.setLevel(db_logger_log_level)


# Migrations
migrate = Migrate(app, db)


# flask-upload images
uploaded_images = UploadSet('images', IMAGES)
configure_uploads(app, uploaded_images)


from gardenDiary import views
from user import views