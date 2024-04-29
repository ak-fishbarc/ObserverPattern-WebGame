from communications.send_email import send_email
from flask import render_template
from abc import ABC, abstractmethod


class NotificationManager:
    def __init__(self, app, mail):
        self.app = app
        self.mail = mail
        self.subscriptions = []

    def subscribe(self, user):
        self.subscriptions.append(user)

    def unsubscribe(self, user):
        self.subscriptions.remove(user)

    def notify(self, subject, news_text, news_html):
        for user in self.subscriptions:
            user.update(self.mail, subject, self.app, news_text, news_html)


class SubscriberInterface(ABC):
    @abstractmethod
    def update(self, mail, subject, app, news_text, news_html):
        pass


class EmailSubscription(SubscriberInterface):
    def __init__(self, email):
        self.email = email

    def update(self, mail, subject, app, news_text, news_html):
        send_email(mail, subject, app.config['MAIL_USERNAME'],
                   [self.email],
                   render_template(news_text),
                   render_template(news_html))

