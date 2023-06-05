from celery import shared_task
from django_celery_beat.models import PeriodicTask
from django.conf import settings

from generalutils.utils import sendEmailMessage
from collectregisters.utils import getReadingsFromSite, getContactsFromSite, getReceiptsFromSite
from main.celery import app

@app.task
def collectReadings():
    file  = getReadingsFromSite()

    if settings.DEBUG == False:
        receipt_to = ['oplata@mail.org056.ru','p.blagovisnyi@mail.org056.ru']
    else:
        receipt_to = ['p.blagovisnyi@mail.org056.ru']

    sendEmailMessage(
        message_title = 'Показания с сайта',
        message_body = 'Показания с сайта во вложении',
        message_file = file,
        message_sender = 'pok@orenburgregiongaz.ru',
        message_recipient = receipt_to
    )

@app.task
def collectContacts():

    file = getContactsFromSite()

    if settings.DEBUG == False:
        receipt_to = ['s.stepanov@mail.org056.ru','p.blagovisnyi@mail.org056.ru']
    else:
        receipt_to = ['p.blagovisnyi@mail.org056.ru']

    sendEmailMessage(
        message_title = 'Контакты с сайта',
        message_body = 'Контакты с сайта во вложении',
        message_file = file,
        message_sender = 'contacts@orenburgregiongaz.ru',
        message_recipient = receipt_to
    )

@app.task
def collectReceipts():
    file = getReceiptsFromSite()
    if settings.DEBUG == False:
        receipt_to = ['s.stepanov@mail.org056.ru','p.blagovisnyi@mail.org056.ru']
    else:
        receipt_to = ['p.blagovisnyi@mail.org056.ru']

    sendEmailMessage(
        message_title = 'Заявки на квитанции с сайта',
        message_body = 'Заявки на квитанции с сайта во вложении',
        message_file = file,
        message_sender = 'zayavki@orenburgregiongaz.ru',
        message_recipient = receipt_to
    )
