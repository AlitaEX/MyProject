from threading import Thread
from app import mail, app
from flask_mail import Message
from flask import current_app, render_template


def send_async_mail(app, msg):
    with app.app_context():
        mail.send(msg)


def send_reset_password_mail(user, token):
    msg = Message("Hello",
                  sender=current_app.config['MAIL_USERNAME'],
                  recipients=[user.email],
                  html=render_template('reset_password_mail.html', user=user, token=token))
    # mail.send(msg)
    Thread(target=send_async_mail, args=(app, msg)).start()