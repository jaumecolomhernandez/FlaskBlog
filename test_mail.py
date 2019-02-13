from flask_mail import Message
from app import mail, app
msg = Message('test subject', sender='ohjaumejaumesdfgsdf@gmail.com', recipients=['jaumecolomhernandez@gmail.com'])
msg.body = 'text body'
msg.html = '<h1>HTML body</h1>'
with app.app_context():
    mail.send(msg)