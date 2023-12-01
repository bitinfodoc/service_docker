
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
        try:
            ls = request.data.get("account_number")
            is_finish = request.data.get("is_finish")
            print(ls)
            print(is_finish)
            contract = ContractVdgo.objects.filter(account_number = ls).first()

            if is_finish == True:
                contract.is_finish = True
            elif is_finish == False:
                contract.is_sended = False
                contract.is_signed = False
                contract.consent = False

            contract.save()

            return HttpResponse(json.dumps({'message': "Updated", "status": True}), status=200)

        except:
            return HttpResponse(json.dumps({'message': "Some error", "status": False}), status=400)


