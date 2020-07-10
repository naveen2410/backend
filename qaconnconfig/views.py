from django.shortcuts import render
from rest_framework import viewsets          # add this
from .serializers import QaconnconfigSerializer      # add this
from .models import Qaconnconfig                     # add this

class QaconnconfigView(viewsets.ModelViewSet):       # add this
    serializer_class = QaconnconfigSerializer          # add this
    queryset = Qaconnconfig.objects.all()              # add this