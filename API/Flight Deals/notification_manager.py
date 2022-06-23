import os
from twilio.rest import Client
import smtplib

class NotificationManager:
    '''Sends the message using twilio api'''

    def send_message(self, messages):
        twilio_sid = os.environ.get("TWILIO_SID")
        twilio_token = os.environ.get("TWILIO_TOKEN")

        client = Client(twilio_sid, twilio_token)
        for message in messages:
            client.messages.create(body=message,
                                   from_=os.environ.get("TWILIO_FROM"),
                                   to=os.environ.get("TWILIO_TO"))

    def send_email(self, messages):
        for message in messages:
            with smtplib.SMTP("smtp.gmail.com", 587, timeout=120) as connection:
                connection.starttls()
                connection.login(user="ticwatch405@gmail.com", password="Conta150xbox")
                connection.sendmail(from_addr="ticwatch405@gmail.com",
                                    to_addrs="nicolasoutrog@gmail.com",
                                    msg=''.join(message).encode('utf-8'))
