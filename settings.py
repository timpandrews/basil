import os

SECRET_KEY = '12345678'
DEBUG = True


# Database Config
DB_USERNAME = 'root'
DB_PASSWORD = 'adam321'
BLOG_DATABASE_NAME = 'basil'
DB_HOST = 'localhost'
DB_URI = "mysql+pymysql://%s:%s@%s/%s" % (DB_USERNAME, DB_PASSWORD, DB_HOST, BLOG_DATABASE_NAME)
SQLALCHEMY_DATABASE_URI = DB_URI
SQLALCHEMY_TRACK_MODIFICATIONS = True