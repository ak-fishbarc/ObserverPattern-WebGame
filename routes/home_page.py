from flask import Blueprint
from flask import render_template


def create_home_page_blueprint(app):
    home_page_bp = Blueprint('home_page', __name__, template_folder='templates')

    @app.route('/')
    @app.route('/home_page')
    def home_page():
        return render_template('home_page.html', title="Web Game")

    return home_page_bp




