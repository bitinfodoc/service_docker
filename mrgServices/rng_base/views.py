from django.shortcuts import render
from rest_framework import viewsets, status
from rest_framework.response import Response
from rng_base.utils import createRngBaseRecord
from .serializers import FileUploadSerializer
from .models import RngBaseRecord

class RngBase(viewsets.ViewSet):
    serializer_class = FileUploadSerializer
    def list(self, request):
        file = 'files/sample.txt'
        # createRngBaseRecord(file)
        return Response({'response_text': 'hello'}, status=status.HTTP_200_OK)
    
    def create(self, request):
        file_uploaded = request.FILES.get('file')
        createRngBaseRecord(file_uploaded)
        # content_type = file_uploaded.content_type
        response = "POST API and you have uploaded a {file_uploaded} file"
        return Response(response)
    
    def delete(self, request):
        RngBaseRecord.objects.all().delete()
        return Response({'All data delited'})