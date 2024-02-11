from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Profile(models.Model):
    username = models.CharField(max_length=300, null=True)
    email = models.EmailField(max_length=254,unique=True, null=True)
    name = models.CharField(max_length=300, null=True)
    phone = models.CharField(max_length=16, null=True,)
    phoneOptional = models.CharField(max_length=16,null=True, blank=True)
    referral = models.ImageField(upload_to='referral/',)
    identity = models.ImageField(upload_to='identity/',)
    auth_token = models.CharField(max_length=100)
    is_verified = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.username 
    
    
class Contact(models.Model):
    name = models.CharField(max_length=150)
    email = models.EmailField(max_length=254,unique=True)
    subject = models.CharField(max_length=500)
    message = models.TextField()
    
    def __str__(self):
        return self.name 
    
    
class ClientEvent(models.Model):
    name = models.CharField(max_length=150)
    email = models.EmailField(max_length=254,unique=True)
    message = models.TextField()
    
    def __str__(self):
        return self.name 