
import os
from django.http import HttpResponse
import json
# import django.conf import settings

# Create your views here.
from django.core.files import File
from django.shortcuts import render
from rest_framework import viewsets, status
from rest_framework.response import Response
from contracts.serializers import ContractResetSerializer
from django.conf import settings
from contracts.models import ContractVdgo
from datetime import datetime

class ContractsVdgoUpdate(viewsets.ViewSet):

    serializer_class = ContractResetSerializer
    def list(self, request):
        return Response({'response_text': 'hello'}, status=status.HTTP_200_OK)

    def retrieve(self, request, pk=None):
        pass

    def create(self, request):
        print('add fileviews')
        serializer = ContractResetSerializer(data=request.data)
        if serializer.is_valid():
            try:
                if request.data.get("token") == "4c53ff6e-d732-4ec9-a94b-19438a0083da":
                    ls = request.data.get("account_number")
                    is_finish = request.data.get("is_finish")
                    is_reset = request.data.get("is_reset")

                    contract = ContractVdgo.objects.filter(account_number = ls).first()

                    if (is_finish == None or is_finish == False) and (is_reset == None or is_reset == False):
                        return HttpResponse(json.dumps({'message': "Введены некорректные данные. Поля finish и reset имеют равные значения или не заданы явно.", "status": False}, ensure_ascii=False), status=401)

                    elif is_reset == True:
                        print("is uncorrect")
                        contract.is_sended = False
                        contract.is_signed = False
                        contract.error_text = "Переданны некорректные данные от абонента"
                        contract.consent = False
                        contract.save()

                    elif is_finish == True:
                        print("is correct")
                        contract.is_finish = True
                        contract.save()

                    else:
                        return HttpResponse(json.dumps({'message': "Введены некорректные данные. Поля finish и reset не заданы явно.", "status": False}, ensure_ascii=False), status=401)

                    return HttpResponse(json.dumps({'message': "Успешно", "status": True}, ensure_ascii=False), status=200)

            except:
                return HttpResponse(json.dumps({'message': "Изменить статусы заявки не удалось", "status": False}, ensure_ascii=False), status=400)
        return HttpResponse(json.dumps({'message': "Изменить статусы заявки не удалось. Получен неверный объект", "status": False}, ensure_ascii=False), status=400)



