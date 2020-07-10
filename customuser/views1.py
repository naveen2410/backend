from django.shortcuts import render
from rest_framework import viewsets          # add this
from .serializers import CustomuserSerializer      # add this
from .models import Customuser                     # add this
from django_filters.rest_framework import DjangoFilterBackend

class CustomuserView(viewsets.ModelViewSet):       # add this
    serializer_class = CustomuserSerializer          # add this
    queryset = Customuser.objects.all()              # add this    
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['user', 'role']