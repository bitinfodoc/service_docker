# from .models import RngBaseRecord
from rest_framework import serializers
# from base.services import delete_old_file
from contracts.models import ContractVdgo

class CntractData(serializers.Serializer):

    account_number = serializers.CharField()
    account_number_rng = serializers.CharField()
    account_address = serializers.CharField()

    passport_name = serializers.CharField()
    passport_place = serializers.CharField()
    passport_birth_date = serializers.CharField()
    passport_serial = serializers.CharField()
    passport_number = serializers.CharField()
    passport_issued_date = serializers.CharField()
    passport_issued = serializers.CharField()
    passport_issued_code = serializers.CharField()
    passport_address_registration = serializers.CharField()

    passport_scan_first = serializers.FileField()
    passport_scan_second = serializers.FileField()

    snils_number = serializers.CharField()
    certificate_first = serializers.FileField()
    certificate_second = serializers.FileField()
    certificate_therd = serializers.FileField()
    certificate_fourth = serializers.FileField()
    certificate_fifth = serializers.FileField()
    certificate_last = serializers.FileField()
    phone = serializers.CharField()
    email = serializers.CharField()
    confirm = serializers.BooleanField()
    consent = serializers.BooleanField()

class FileUploadSerializer(serializers.Serializer):
    file = serializers.FileField()
    class Meta:
        fields = ['file_uploaded']

