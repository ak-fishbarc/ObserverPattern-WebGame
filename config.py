import os


class Config:
    """ GENERAL CONFIG """
    SECRET_KEY = os.environ.get('PROJECT_KEY')
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL')

    """ MAIL CONFIG"""
    MAIL_SERVER = os.environ.get('MAIL_SERVER')
    MAIL_PORT = os.environ.get('MAIL_PORT')
    MAIL_USE_TLS = os.environ.get('MAIL_USE_TLS')
    MAIL_USERNAME = os.environ.get('MAIL_USERNAME')
    MAIL_PASSWORD = os.environ.get('MAIL_PASSWORD')


