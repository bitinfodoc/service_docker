from django.shortcuts import render
from rest_framework import viewsets, status
from rest_framework.response import Response
from .serializers import FileUploadSerializer, FileValidateSerializer
from lsvalidate.models import LsRecord
from lsvalidate.tasks import ls_upload
# Create your views here.


class LsUpload(viewsets.ViewSet):
    serializer_class = FileUploadSerializer
    def list(self, request):
        return Response({'response_text': 'hello'}, status=status.HTTP_200_OK)

    def create(self, request):
        file_uploaded = request.FILES.get('file')
        file_lines = file_uploaded.read().decode().splitlines()
        ls_upload.delay(file_lines)
        response = f"POST API and you have uploaded a {file_uploaded} file"
        return Response(response)

    def delete(self, request):
        LsRecord.objects.all().delete()
        return Response({'All data delited'})


class LsValidate(viewsets.ViewSet):
    serializer_class = FileValidateSerializer

    def list(self, request):
        return Response({'response_text': 'hello'}, status=status.HTTP_200_OK)

    def post(self, request):

        ls = request.data.get('ls')

        if len(ls) == 8:
            ls_record = LsRecord.objects.filter(account_number = ls)
        else:
            ls_record = LsRecord.objects.filter(account_number_rng = ls)

        response = False
        if len(ls_record) !=0:
            response = True

        return Response(response)