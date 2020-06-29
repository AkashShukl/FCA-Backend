import os

basedir = os.path.abspath(os.path.dirname(__file__))


class Config(object):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = os.environ['DATABASE_URL'] or 'sqlite:///' + os.path.join(basedir, 'app.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    CSRF_ENABLED = True


class DevelopmentConfig(Config):
    #SQLALCHEMY_DATABASE_URI = os.environ['DATABASE_URL'] or 'sqlite:///' + os.path.join(basedir, 'app.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    DEBUG = True


# Adding some lines in order to perform testing might delete later

class TestingConfig(Config):
    TESTING = True
    #SQLALCHEMY_DATABASE_URI = 'postgres://admin:password@localhost/test_db'
    DEBUG = True


# # my db URL: postgresql+psycopg2://admin:password@localhost/markmail'

app_config = {
    'Config': Config,
    'testing': TestingConfig,
    'development': DevelopmentConfig,
}