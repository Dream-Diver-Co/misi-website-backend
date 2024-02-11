from django.shortcuts import render
from .models import *
from rest_framework import permissions, viewsets
from .serializers import *
# Create your views here.
class ProfileViewSet(viewsets.ModelViewSet):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer
    permission_classes = [permissions.IsAuthenticated]
    
    
class ContactViewSet(viewsets.ModelViewSet):
    queryset = Contact.objects.all()
    serializer_class = ContactSerializer
    permission_classes = [permissions.IsAuthenticated]
    
    
class ClientEventViewSet(viewsets.ModelViewSet):
    queryset = ClientEvent.objects.all()
    serializer_class = ClientEventSerializer
    permission_classes = [permissions.IsAuthenticated]