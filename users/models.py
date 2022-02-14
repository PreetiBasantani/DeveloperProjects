

from django.db import models
from django.contrib.auth.models import User



# Create your models here.

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True,blank=True)

    name = models.CharField(max_length=200, null=True,blank=True)
    username = models.CharField(max_length=200, null=True,blank=True)
    profile_location = models.CharField(max_length=100, null=True,blank=True)
    email = models.EmailField(null=True,blank=True)
    short_intro =models.CharField(max_length=1000, null=True,blank=True)
    bio = models.TextField(null=True,blank=True)
    profile_image = models.ImageField(upload_to='profiles/',default='profiles.user-default.png')
    social_github = models.CharField(max_length=2000, null=True,blank=True)
    social_twitter = models.CharField(max_length=2000, null=True,blank=True)
    social_youtube = models.CharField(max_length=2000, null=True,blank=True)
    social_linkedin = models.CharField(max_length=2000, null=True,blank=True)
    social_website = models.CharField(max_length=2000, null=True,blank=True)
    # created = models.DateTimeField(auto_now_add=True,)

    def __str__(self):
        return self.name



class Skill(models.Model):
    owner = models.ForeignKey(Profile,on_delete=models.CASCADE,null=True,blank=True)
    name = models.CharField(max_length=100, null=True,blank=True)
    description = models.TextField (null=True,blank=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


