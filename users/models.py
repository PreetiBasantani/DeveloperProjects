import email
from email.policy import default
from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Profile(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE,null=True,blank=True)
    name= models.CharField(max_length=200,null=True,blank=True)
    username = models.CharField(max_length=200,null=True,blank=True)
    email = models.EmailField(blank=True,null=True)
    short_intro = models.CharField(max_length=200,null=True,blank=True)
    bio = models.TextField(null=True,blank=True)
    profile_image = models.ImageField(upload_to = 'profiles/',default='user-default.png' )
    social_github = models.CharField(max_length=200,null=True,blank=True)
    social_twitter = models.CharField(max_length=200,null=True,blank=True)
    social_youtube = models.CharField(max_length=200,null=True,blank=True)
    social_linkedin = models.CharField(max_length=200,null=True,blank=True)
    social_website = models.CharField(max_length=200,null=True,blank=True)

    def __str__(self): 
        return str(self.user.username)