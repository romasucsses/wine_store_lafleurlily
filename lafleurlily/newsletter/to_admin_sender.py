from twilio_api.msg_to_phone import send_message
from orders.models import OrderInformation
from accounts.models import User

NUMBER_OF_ADMIN = '37367580565'


def new_order_without_payment():
    msg_body = f'Get the order {OrderInformation.pk} without payment at moment'
    return send_message(number=NUMBER_OF_ADMIN, message=msg_body)


def checkout_is_payment():
    msg_body = f'Get the order {OrderInformation.pk} without payment at moment'
    return send_message(number=NUMBER_OF_ADMIN, message=msg_body)


def new_user_registration():
    msg_body = f'Registered the New User on site: {User.email}'
    return send_message(number=NUMBER_OF_ADMIN, message=msg_body)


