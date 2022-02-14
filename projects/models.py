from email.policy import default
from django.utils import timezone
from django.db import models

# Create your models here.

class Project(models.Model):
    title = models.CharField(max_length=200) 
    image = models.ImageField(upload_to='photos/',null=True ,blank=True, default='website.jpg')
    description = models.TextField(null=True,blank=True)
    demo_link = models.CharField(max_length=2000,null=True,blank=True)
    source_link= models.CharField(max_length=2000,null=True,blank=True)
    tags = models.ManyToManyField('Tag',blank=True)
    created = models.DateTimeField(auto_now_add=True)
    published = models.DateTimeField(default = timezone.now)
    vote_total = models.IntegerField(default=0,blank=True,null=True)
    vote_ratio = models.IntegerField(default=0,blank=True,null=True)


    def __str__(self):
        return self.title


class Review(models.Model):
    Vote_type = [('up','Up Vote'),
                 ('down','Down Vote'),
                ]

    project = models.ForeignKey(Project,on_delete=models.CASCADE)
    body = models.TextField(null=True,blank=True)
    value = models.CharField(max_length=100,choices=Vote_type)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.value
    

class Tag(models.Model):

    name = models.CharField(max_length=100)
    created = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return self.name
