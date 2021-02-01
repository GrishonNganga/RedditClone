class DevConfig:
    DEBUG = True
    TESTING = True
    ENV = 'development'
    SQLALCHEMY_DATABASE_URI = "mysql+pymysql://root:@localhost/redditt"
    SECRET_KEY = 'something_super_super_secret'


class Prod:
    DEBUG = False
    ENV = 'production'


config = {
    'dev': DevConfig,
    'prod': Prod
}