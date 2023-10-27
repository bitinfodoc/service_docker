
import os
from django.http import HttpResponse
import json
# import django.conf import settings

# Create your views here.
from django.core.files import File
from django.shortcuts import render
from django.shortcuts import render
from rest_framework import viewsets, status
from rest_framework.response import Response
from contracts.serializers import CntractData, FileUploadSerializer
from contracts.tasks import createContractVdgoRecord
from django.conf import settings
from contracts.models import ContractVdgo

class ContractsVdgoUpload(viewsets.ViewSet):

    serializer_class = FileUploadSerializer
    def list(self, request):

        return Response({'response_text': 'hello'}, status=status.HTTP_200_OK)

    def create(self, request):

        file_uploaded = request.FILES.get('file')
        file_lines = file_uploaded.read().decode().splitlines()
        createContractVdgoRecord.delay(file_lines)
        # response = f"POST API and you have uploaded a {file_uploaded} file"


        return HttpResponse(json.dumps({'message': "Uploaded"}), status=200)


# Create your views here.
class ContractsVdgoView(viewsets.ViewSet):

    serializer_class = CntractData


    def list(self, request):

        return Response({'response_text': 'hello'}, status=status.HTTP_200_OK)


    def create(self, request):
        return HttpResponse(json.dumps({'message': "Uploaded"}), status=200)

    def update(self, request, pk=None):

        # file_uploaded = request.data['passport_scan_first']
        # basename = os.path.basename(self.file_uploaded)
        # print(basename)
        # File(open(file_uploaded, 'rb'))

        # out = open("img.png", "wb")
        # out.write(file_uploaded.read().decode())
        # out.close

        print(request.data)
        print(request.data.get('account_number'))
        # print(request.data['passport_scan_first'])
        print(request.data.get("passport_scan_first"))
        print(request.FILES.get('passport_scan_second'))

        contract = ContractVdgo.objects.get(account_number=pk)

        # фио в паспорте
        if request.data.get('passport_name'):
            contract.passport_name = request.data.get('passport_name')

        # место рождения
        if request.data.get('passport_place'):
            contract.passport_place = request.data.get('passport_place')

        # дата рождения
        if request.data.get('passport_birth_date'):
            contract.passport_birth_date = request.data.get('passport_birth_date')

        # серия паспорта
        if request.data.get('passport_serial'):
            contract.passport_serial = request.data.get('passport_serial')

        # номер паспорта
        if request.data.get('passport_number'):
            contract.passport_number = request.data.get('passport_number')

        # дата выдачи
        if request.data.get('passport_issued_date'):
            contract.passport_issued_date = request.data.get('passport_issued_date')

        # кем выдан
        if request.data.get('passport_issued'):
            contract.passport_issued = request.data.get('passport_issued')

        # код подразделения
        if request.data.get('passport_issued_code'):
            contract.passport_issued_code = request.data.get('passport_issued_code')

        # адрес прописки
        if request.data.get('passport_address_registration'):
            contract.passport_address_registration = request.data.get('passport_address_registration')

        # скан первой страницы паспорта
        if request.FILES.get('passport_scan_first'):
            contract.passport_scan_first = request.FILES.get('passport_scan_first')

        # скан второй страницы паспорта
        if request.FILES.get('passport_scan_second'):
            contract.passport_scan_second = request.FILES.get('passport_scan_second')


        # номер снилс
        if request.data.get('snils_number'):
            contract.snils_number = request.data.get('snils_number')

        # скан Снилс
        if request.FILES.get('snils_first'):
            contract.snils_first = request.FILES.get('snils_first')


        # номер инн
        if request.data.get('inn_number'):
            contract.inn_number = request.data.get('inn_number')

        # скан инн
        if request.FILES.get('inn_first'):
            contract.inn_first = request.FILES.get('inn_first')

        # скан ЕГРН
        if request.FILES.get('certificate_first'):
            contract.certificate_first = request.FILES.get('certificate_first')
        if request.FILES.get('certificate_second'):
            contract.certificate_second = request.FILES.get('certificate_second')
        if request.FILES.get('certificate_therd'):
            contract.certificate_therd = request.FILES.get('certificate_therd')
        if request.FILES.get('certificate_fourth'):
            contract.certificate_fourth = request.FILES.get('certificate_fourth')
        if request.FILES.get('certificate_fifth'):
            contract.certificate_fifth = request.FILES.get('certificate_fifth')
        if request.FILES.get('certificate_last'):
            contract.certificate_last = request.FILES.get('certificate_last')


        # номер телефона
        if request.data.get('phone'):
            contract.phone = request.data.get('phone')

        # емаил
        if request.data.get('email'):
            contract.email = request.data.get('email')

        # согласие
        if request.data.get('confirm'):
            contract.confirm = request.data.get('confirm')

        # подтверждение
        if request.data.get('consent'):
            contract.consent = request.data.get('consent')

        contract.save()

        return Response(json.dumps({'message': "Uploaded"}), status=200)

    def delete(self, request):
        response_text = 'No DEBUG. No data delited.'
        if settings.DEBUG == 1:
            LsRecord.objects.all().delete()
            response_text = 'All data delited'
        return Response({response_text})