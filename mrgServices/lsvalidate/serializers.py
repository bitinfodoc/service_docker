# from .models import RngBaseRecord
from rest_framework import serializers


class FileUploadSerializer(serializers.Serializer):
    file = serializers.FileField()
    class Meta:
        fields = ['file_uploaded']

class FileValidateSerializer(serializers.Serializer):
    ls = serializers.CharField()