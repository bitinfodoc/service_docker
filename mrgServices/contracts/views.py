
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
from contracts.tasks import create_contract_record, copy_to_network
from django.conf import settings
from contracts.models import ContractVdgo
from datetime import datetime

class ContractsVdgoUpload(viewsets.ViewSet):

    serializer_class = FileUploadSerializer
    def list(self, request):

        return Response({'response_text': 'hello'}, status=status.HTTP_200_OK)

    def retrieve(self, request, pk=None):

        if pk == 'send':
            copy_to_network.delay()
            return Response({'message': "Sended"}, status=200)

    def create(self, request):
        print('add fileviews')

        file_uploaded = request.FILES.get('file')
        file_lines = file_uploaded.read().decode().splitlines()

        create_contract_record.delay(file_lines)
        # response = f"POST API and you have uploaded a {file_uploaded} file"
        return HttpResponse(json.dumps({'message': "Uploaded"}), status=200)


# Вьюс для Контрактов.
class ContractsVdgoView(viewsets.ViewSet):

    serializer_class = CntractData


    def list(self, request):
        ls = request.GET.get("ls")
        print(ls)
        return Response({'response_text': 'hello'}, status=status.HTTP_200_OK)


    def create(self, request):
        ls = str(request.data.get('account_number'))
        self.update_contracts_vdgo(request, ls)
        return HttpResponse(json.dumps({'message': "Uploaded"}), status=200)

    def retrieve(self, request, pk=None):

        if len(pk) == 8: queryset = ContractVdgo.objects.filter(account_number = pk)
        else: queryset = ContractVdgo.objects.filter(account_number_rng = pk)

        if len(queryset) == 0:
            response = False
            return Response(response, status=204)
        else:
            contract = queryset.first()
            if contract.consent == True:
                response = True
                return Response(response, status=208)
            else:
                return Response(contract.account_address, status=200)


    def update(self, request, pk=None):

        # file_uploaded = request.data['passport_scan_first']
        # basename = os.path.basename(self.file_uploaded)
        # print(basename)
        # File(open(file_uploaded, 'rb'))

        # out = open("img.png", "wb")
        # out.write(file_uploaded.read().decode())
        # out.close

        self.update_contracts_vdgo(request, pk )

        return Response(json.dumps({'message': "Uploaded"}), status=200)

    def delete(self, request):
        response_text = 'No DEBUG. No data delited.'
        if settings.DEBUG == 1:
            ContractVdgo.objects.all().delete()
            response_text = 'All data delited'
        return Response({response_text})

    def extension_file(self, file):
        name, extension = os.path.splitext(file.name)
        return extension

    def update_contracts_vdgo(self, request, account_number):

        if len(account_number) == 8: contract = ContractVdgo.objects.get(account_number = account_number)
        else: contract = ContractVdgo.objects.get(account_number_rng = account_number)

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
            contract.passport_scan_first.delete(save=False)
            contract.passport_scan_first = request.FILES.get('passport_scan_first')
            contract.passport_scan_first.name = "pass_1_" + account_number + self.extension_file(request.FILES.get('passport_scan_first'))

        # скан второй страницы паспорта
        if request.FILES.get('passport_scan_second'):
            contract.passport_scan_second.delete(save=False)
            contract.passport_scan_second = request.FILES.get('passport_scan_second')
            contract.passport_scan_second.name = "pass_2_" + account_number + self.extension_file(request.FILES.get('passport_scan_second'))


        # номер снилс
        if request.data.get('snils_number'):
            contract.snils_number = request.data.get('snils_number')

        # скан Снилс
        if request.FILES.get('snils_first'):
            contract.snils_first.delete(save=False)
            contract.snils_first = request.FILES.get('snils_first')
            contract.snils_first.name = "snils_first_" + account_number + self.extension_file(request.FILES.get('snils_first'))


        # номер инн
        if request.data.get('inn_number'):
            contract.inn_number = request.data.get('inn_number')

        # скан инн
        if request.FILES.get('inn_first'):
            contract.inn_first.delete(save=False)
            contract.inn_first = request.FILES.get('inn_first')
            contract.inn_first.name = "inn_" + account_number + self.extension_file(request.FILES.get('inn_first'))

        # скан ЕГРН
        if request.FILES.get('certificate_first'):
            contract.certificate_first.delete(save=False)
            contract.certificate_first = request.FILES.get('certificate_first')
            contract.certificate_first.name = "certificate_first_" + account_number + self.extension_file(request.FILES.get('certificate_first'))
        if request.FILES.get('certificate_second'):
            contract.certificate_second.delete(save=False)
            contract.certificate_second = request.FILES.get('certificate_second')
            contract.certificate_second.name = "certificate_second_" + account_number + self.extension_file(request.FILES.get('certificate_second'))
        if request.FILES.get('certificate_therd'):
            contract.certificate_therd.delete(save=False)
            contract.certificate_therd = request.FILES.get('certificate_therd')
            contract.certificate_therd.name = "certificate_therd_" + account_number + self.extension_file(request.FILES.get('certificate_therd'))
        if request.FILES.get('certificate_fourth'):
            contract.certificate_fourth.delete(save=False)
            contract.certificate_fourth = request.FILES.get('certificate_fourth')
            contract.certificate_fourth.name = "certificate_fourth_" + account_number + self.extension_file(request.FILES.get('certificate_fourth'))
        if request.FILES.get('certificate_fifth'):
            contract.certificate_fifth.delete(save=False)
            contract.certificate_fifth = request.FILES.get('certificate_fifth')
            contract.certificate_fifth.name = "certificate_fifth_" + account_number + self.extension_file(request.FILES.get('certificate_fifth'))
        if request.FILES.get('certificate_last'):
            contract.certificate_last.delete(save=False)
            contract.certificate_last = request.FILES.get('certificate_last')
            contract.certificate_last.name = "certificate_last_" + account_number + self.extension_file(request.FILES.get('certificate_last'))


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

        contract.last_update_date = datetime.now()

        contract.save()