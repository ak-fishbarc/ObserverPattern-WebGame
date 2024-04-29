from flask import Blueprint
from flask import render_template
from flask_login import current_user
import json

import communications.subscription_form as sf
from communications.notification_manager import EmailSubscription


def create_news_board_blueprint(app, db, nosql_db, user_model, mail, notification_manager):
    news_board_bp = Blueprint('news_board', __name__, template_folder='templates')

    @app.route('/news_board/')
    @app.route('/news_board/<page_number>')
    def news_board(page_number=0):
        number_of_pages = 0
        paginate_by = 10
        # Generated news for testing.
        news = {"name": "Somenews", "address": "/event_news/event_sale", "image": "/static/news_image.png"}
        # Change news_to_flash to Json for parsing by news_flash.js
        news_to_flash = [news for i in range(0, 5)]
        news_to_flash = json.dumps(news_to_flash)

        news_to_show = [news for i in range(0, 32)]
        # Divide news by specified number to get desired number of news per page.
        if int(len(news_to_show) % paginate_by) != 0:
            number_of_pages = int(len(news_to_show)/paginate_by) + 1
        else:
            number_of_pages = int(len(news_to_show)/paginate_by)

        # If page number == 0, get first amount of news specified by paginate_by value.
        # To get the index of next page, multiply page number by paginate_by value.
        # If paginate_by == 10, e.g. Page 1; Start from index 10. Page 2; Start from index 20.
        paginate_news = (int(page_number) * paginate_by)
        # Get desired number of news starting from the paginate_news index.
        # If page == 2. Start from index 2 * paginate_by value and get news up to index equal to paginate_by value.
        # E.g. if paginate_by == 10 and page == 2. Start from index 20 and finish on index 30.
        limit_to = (int(paginate_news) + paginate_by)
        paginated_news = news_to_show[paginate_news:limit_to]
        number_of_pointers = range(0, number_of_pages)
        return render_template('news_board.html', news_to_show=paginated_news, number_of_pages=number_of_pointers,
                               news_to_flash=news_to_flash)

    @app.route('/event_news/<event_id>')
    def event_news(event_id):
        # I did not wanted to create routes for all the news separately.
        # This bit of code will read html files from templates/news/ folder and send it
        # to /event_news/ route for Javascript to generate page elements out of it.
        # This adds some flexibility to news system.

        with open("./templates/news/" + event_id + ".html") as template:
            event_template = str(template.read())
        return render_template('event_news.html', event_template=event_template)

    @app.route('/news_subscription', methods=["POST", "GET"])
    def news_subscription():
        form = sf.SubscriptionForm()
        if form.validate_on_submit():
            if current_user.username not in notification_manager.subscriptions:
                subscribe_user = EmailSubscription(current_user.email)
                notification_manager.subscribe(subscribe_user)
                # Here for trial
                notification_manager.notify("News For You",
                                            'news/event_sale.html',
                                            'news/event_sale.html')
        return render_template('news_subscription.html', form=form)

    return news_board_bp

