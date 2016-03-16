from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy
from flask.ext.migrate import Migrate
from sqlalchemy import create_engine

app = Flask(__name__)
app.config.from_object('settings')
db = SQLAlchemy(app)

sql = create_engine(app.config['DB_URI'], pool_size=20, max_overflow=0, pool_recycle=300)


# Migrations
migrate = Migrate(app, db)

from gardenDiary import views
from user import views