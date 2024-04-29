from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate, init, upgrade, migrate
from flask_mail import Mail
from flask_pymongo import PyMongo
from flask_login import LoginManager

from routes import login_and_registration as lar
from routes import home_page as hp
from routes import reset_password as rp
from routes import player_profile as pp
from routes import news_board as nb


#########################################
#                                       #
#       FLASK Creation Functions        #
#                                       #
#########################################


def create_app(config):
    app = Flask(__name__)
    app.config.from_object(config)

    return app


def create_blueprints(app, db, nosql_db, user_model, mail, notification_manager):
    app.register_blueprint(hp.create_home_page_blueprint(app))
    app.register_blueprint(lar.create_login_and_registration_blueprint(app, db, nosql_db, user_model, mail))
    app.register_blueprint(rp.create_reset_password_blueprint(app, db, user_model, mail))
    app.register_blueprint(pp.create_player_pages_blueprint(app, db, nosql_db, user_model, mail, notification_manager))
    app.register_blueprint(nb.create_news_board_blueprint(app, db, nosql_db, user_model, mail, notification_manager))


def create_login(app):
    login_mg = LoginManager(app)

    return login_mg


def create_mail(app):
    mail = Mail(app)

    return mail


######################################
#                                    #
#       SQL Creation Functions       #
#                                    #
######################################

def create_db(app):
    sql_db = SQLAlchemy(app)

    return sql_db


def create_models(app, db):
    with app.app_context():
        db.create_all()
        db.session.commit()


def create_migrate(app, db):
    migration = Migrate(app, db)
    return migration


def initialize_migration(app):
    with app.app_context():
        init()


def db_migrate(app):
    with app.app_context():
        migrate()


def db_migrate_upgrade(app):
    with app.app_context():
        upgrade()


#########################################
#                                       #
#       NOSQL Creation Functions        #
#                                       #
#########################################


def create_mongodb(app):
    mongo_db = PyMongo(app)

    return mongo_db


