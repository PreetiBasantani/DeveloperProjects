from django.db import models
from django.utils import timezone
from users.models import Profile

# Create your models here.

class Project(models.Model):
    
    owner = models.ForeignKey(Profile,on_delete=models.SET_NULL, null=True)  
    name = models.CharField(max_length=200)
    description = models.TextField(null=True,blank=True)
    #Form doesn't require a value and database also doesn't require a value
    # OR default = timezone.now 
    
    demo_link = models.CharField(max_length=2000,null=True,blank=True)
    source_link = models.CharField(max_length=2000,null=True,blank=True)
    
    created  = models.DateTimeField(auto_now_add=True)
  
    tags = models.ManyToManyField('Tag',blank=True)                                                                 
    img = models.ImageField(upload_to ='photos/%Y/%m/%d/',default='code.jpg' )  #photos dir will be created under media folder specified in MEDIA_ROOT variable in settings.py
          
    published_at = models.DateTimeField(default = timezone.now,null=True,blank=True)
    vote_total = models.IntegerField(default = 0,blank=True,null=True)
    vote_ratio = models.IntegerField(default = 0,blank=True,null=True)

    
    def __str__(self):
        return self.name


    
class Review(models.Model):
    VOTE_TYPE =[
                ('up','Up Vote'),
                ('down','Down Vote')
                ]

    #OWNER
    project = models.ForeignKey(Project,on_delete=models.CASCADE)
    body = models.TextField(null=True,blank=True)
    value = models.CharField(max_length=100, choices=VOTE_TYPE)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.value


    
class Tag(models.Model):
    name = models.CharField(max_length=200)
    created = models.DateTimeField(auto_now_add=True)
    # projects = models.ManyToManyField(Project,blank=True)

    def __str__(self):
        return self.name

