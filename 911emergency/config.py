import os

basedir = os.path.abspath(os.path.dirname(__file__))

class Auth:
    CLIENT_ID = ('172252254677-2dkr49b0b736blrgbs6a5g5q7drpjqv4.apps.googleusercontent.com')
    CLIENT_SECRET = 'bZLZjmpcZ_A_AgqtkUZFc7X2'
    REDIRECT_URI = 'https://127.0.0.1:5000/oauth2callback'
    AUTH_URI = 'https://accounts.google.com/o/oauth2/auth'
    TOKEN_URI = 'https://accounts.google.com/o/oauth2/token'
    USER_INFO = 'https://www.googleapis.com/userinfo/v2/me'


class Config:
    APP_NAME = "Test Google Login"
    SECRET_KEY = os.environ.get("SECRET_KEY") or "somethingsecret"


class DevConfig(Config):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, "test.db")


class ProdConfig(Config):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, "prod.db")


config = {
    "dev": DevConfig,
    "prod": ProdConfig,
    "default": DevConfig
}