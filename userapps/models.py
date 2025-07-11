from django.db import models
from django.contrib.auth.models import User

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE) 
    fullname = models.CharField(max_length=50)
    phone = models.CharField(max_length=50)
    gender = models.CharField(max_length=50)
    profile_pix = models.ImageField(upload_to='userpix', default='https://cdn-icons-png.flaticon.com/128/456/456212.png')

    def __str__(self):
        return self.fullname

    
