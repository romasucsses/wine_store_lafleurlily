from twilio.rest import Client
from twilio_api.config import*


def send_message(number, message):
    client = Client(ACCOUNT_SID, AUTH_TOKEN)
    client.messages.create(
        body=message,
        from_='+13203773702',
        to='+' + number
    )
