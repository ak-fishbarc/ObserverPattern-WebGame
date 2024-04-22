from notifypy import Notify


def send_notification(header, body):
    notification = Notify()
    notification.title = header
    notification.message = body
    notification.send()

