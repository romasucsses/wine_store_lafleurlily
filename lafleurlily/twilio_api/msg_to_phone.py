from twilio.rest import Client
from config import*


class SenderMsgToPhone:
    Number = None
    Message = None
    client = Client(ACCOUNT_SID, AUTH_TOKEN)

    def send_messages(self, number, message):
        self.client.messages.create(
            body=self.Message,
            from_='+13203773702',
            to='+' + self.Number
        )