import os

SECRET_KEY = '12345678'
DEBUG = True


# Database Config
DB_USERNAME = 'root'
DB_PASSWORD = 'adam321'
DB_DATABASE_NAME = 'basil'
DB_HOST = 'localhost'
DB_URI = "mysql+pymysql://%s:%s@%s/%s" % (DB_USERNAME, DB_PASSWORD, DB_HOST, DB_DATABASE_NAME)
SQLALCHEMY_DATABASE_URI = DB_URI
SQLALCHEMY_TRACK_MODIFICATIONS = True


# Uploading Media
UPLOADED_IMAGES_DEST = '/Users/timandrews/Desktop/apps/basil/static/usrMedia'
UPLOADED_IMAGES_URL = '/static/usrMedia/'

# SQLAlchemy Paginate
DEFAULT_ENTRIES_PER_PAGE = 5