from django.shortcuts import render
from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.decorators import action
from .models import Csat_filtred_phones
from .serializers import FiltredPhonesSerializer
from .models import Csat_filtred_phones

class FiltredPhonesViewSet(viewsets.ModelViewSet):
    queryset = Csat_filtred_phones.objects.all()
    serializer_class = FiltredPhonesSerializer

