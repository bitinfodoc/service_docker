from django.shortcuts import render
from rest_framework import viewsets, status
from rest_framework.response import Response
from generalutils.utils import sendEmailMessage
from collectregisters.utils import getReadingsFromSite, getContactsFromSite
from datetime import datetime

from django.http import HttpResponse


class getReadings(viewsets.ViewSet):

    def list(self, request):

        print('hello views')
        file = getReadingsFromSite()

        sendEmailMessage(
            message_title = 'Показания с сайта',
            message_body = 'Показания с сайта во вложении',
            message_file = file,
            message_sender = 'pok@orenburgregiongaz.ru',
            message_recipient = ['p.blagovisnyi@mail.org056.ru']
        )

        return Response({'response_text': 'hello'}, status=status.HTTP_200_OK)

class getContacts(viewsets.ViewSet):

    def list(self, request):

        print('hello views')
        file = getContactsFromSite()

        sendEmailMessage(
            message_title = 'Сбор контактов с сайта',
            message_body = 'Контакты с сайта во вложении',
            message_file = file,
            message_sender = 'contacts@orenburgregiongaz.ru',
            message_recipient = ['p.blagovisnyi@mail.org056.ru']
        )

        return Response({'response_text': 'hello'}, status=status.HTTP_200_OK)


