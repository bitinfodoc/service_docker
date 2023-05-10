from django.shortcuts import render
from rest_framework import viewsets, status
from rest_framework.response import Response
from generalutils.utils import sendEmailMessage
from collectregisters.utils import getReadingsFromSite
from datetime import datetime

from django.http import HttpResponse


class getReadings(viewsets.ViewSet):
    # serializer_class = FileUploadSerializer

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

# Create your views here.
# def getReadings(request):
#     res = getReadingsFromSite()
#     print(res)
#     return HttpResponse('hello response')



# функция получения данных из таблицы

