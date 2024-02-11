from .models import *
from rest_framework import serializers

class ProfileSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Profile
        
        fields = ['url','id','username', 'name', 'phone','phoneOptional','referral','identity']
class ContactSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Contact
        
        fields = ['url','id','name','email','subject','message']
class ClientEventSerializer(serializers.HyperlinkedModelSerializer):        
    class Meta:
        model = ClientEvent
        
        fields = ['url','id','name','email','message']