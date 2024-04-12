from flask import Flask
from config import Config
from routes import login_and_registration as lar
from routes import home_page as hp


def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)
    
    app.register_blueprint(hp.create_home_page_blueprint())
    app.register_blueprint(lar.create_login_and_registration_blueprint())

    return app


if __name__ == '__main__':
    create_app().run(debug=True)