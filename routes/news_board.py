from flask import Blueprint
from flask import render_template, redirect, url_for


def create_news_board_blueprint(app, db, nosql_db, user_model, mail):
    news_board_bp = Blueprint('news_board', __name__, template_folder='templates')

    @app.route('/news_board')
    def news_board():
        return render_template('news_board.html')

    return news_board_bp
