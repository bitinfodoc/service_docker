from django.core.mail import send_mail, EmailMessage

def sendEmailMessage(
    message_title = 'Письмо с сервера терминалов',
    message_body = '',
    message_file = None,
    message_sender = 'intokno@mail.org056.ru',
    message_recipient = ['p.blagovisnyi@mail.org056.ru']
    ):

    email = EmailMessage(
        message_title,
        message_body,
        message_sender,
        message_recipient,
    )

    if (message_file != None):
        email.attach_file(message_file)

    try:
        email.send()
        result = { 'status': 0, }
    except:
        result = { 'status': 1, }

    return result