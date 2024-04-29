from flask import render_template
from flask_mail import Message


def send_email(mail, subject, sender, recipients, text_body, html_body):
    msg = Message(subject, sender=sender, recipients=recipients)
    msg.body = text_body
    msg.html = html_body
    mail.send(msg)


def send_password_reset_email(mail, app, user):
    token = user.get_reset_password_token(app)
    send_email(mail, 'Reset Password', app.config['MAIL_USERNAME'], [user.email],
               render_template('reset_password_msg.html', user=user, token=token),
               render_template('reset_password_msg.html', user=user, token=token))



