import os

basedir = os.path.abspath(os.path.dirname(__file__))


class Config(object):

    # SECRET KEY
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'A-VERY-LONG-SECRET-KEY'

    # RECAPTCHA PUBLIC KEY
    RECAPTCHA_PUBLIC_KEY = os.environ.get('RECAPTCHA_PUBLIC_KEY') or 'A-VERY-LONG-SECRET-KEY'
    RECAPTCHA_PRIVATE_KEY = os.environ.get('RECAPTCHA_PRIVATE_KEY') or 'A-VERY-LONG-SECRET-KEY'

    # Database configuration

    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or 'sqlite:///' + os.path.join(basedir, 'app.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    # Flask Gmail Config
    MAIL_SERVER = 'smtp.gmail.com'
    MAIL_PORT = 465
    MAIL_USE_SSL = True
    # 寄信功能ok(flaskex999 測試用Gmail)
    MAIL_USERNAME = os.environ.get('GMAIL_USERNAME') or 'flaskex999@gmail.com'
    MAIL_PASSWORD = os.environ.get('GMAIL_PASSWORD') or 'icrwrdvdiphqqicd'
