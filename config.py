
class Config(object):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = "sqlite:///movies.db"
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    JSON_AS_ASCII = False
    HOST = "localhost"
    PORT = 5000
