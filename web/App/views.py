from django.shortcuts import render

# Create your views here.
import os
from django.conf import settings
from rest_framework import views
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.parsers import JSONParser
from rest_framework.reverse import reverse_lazy
import requests
import json
from django.core import serializers
from rest_framework import generics
from .models import Courtpdfprocesstion
from .serializers import CourtpdfprocesstionSerializer, RequestjsonSerializer
from django.http import HttpResponse

class MetaDataList(generics.ListCreateAPIView):
    queryset = Courtpdfprocesstion.objects.all()
    serializer_class = CourtpdfprocesstionSerializer

class MetaDataDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Courtpdfprocesstion.objects.all()
    serializer_class = CourtpdfprocesstionSerializer

class UserList(APIView):
    def post(self, request, format=None):
        Courtnamefrompostreq = request.query_params['Court']
        Startdatefrompostreq = request.query_params['start_end']
        Enddatefrompostreq = request.query_params['end_date']
        queryset = Courtpdfprocesstion.objects.filter(Court_Name__contains=Courtnamefrompostreq).filter(Judgement_Date__range=(Startdatefrompostreq, Enddatefrompostreq))
        serializer = CourtpdfprocesstionSerializer(queryset, many=True)
        return Response(serializer.data)
        '''
        If using simple django framework
        querysetjson = serializers.serialize('json', queryset)
        return HttpResponse(querysetjson, content_type='application/json')
        '''