from flask import Blueprint
from flask import render_template


def create_news_board_blueprint(app, db, nosql_db, user_model, mail):
    news_board_bp = Blueprint('news_board', __name__, template_folder='templates')

    @app.route('/news_board/')
    @app.route('/news_board/<page_number>')
    def news_board(page_number=0):
        news = {"name": "Somenews", "address": "Someaddress", "image": "/static/news_image.png"}
        news_to_show = [news for i in range(0, 100)]
        number_of_pages = int(len(news_to_show)/10)
        if int(page_number) > number_of_pages:
            return "No more news"
        else:
            paginate_news = (int(page_number) * 10)
            limit_to = (int(paginate_news) + 10)
            paginated_news = news_to_show[paginate_news:limit_to]
            number_of_pointers = range(0, number_of_pages)
        return render_template('news_board.html', news_to_show=paginated_news, number_of_pages=number_of_pointers)

    return news_board_bp
