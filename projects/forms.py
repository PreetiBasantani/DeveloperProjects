from django.forms import ModelForm, models
from  .models import Project

class ProjectForm(ModelForm):
    class Meta:
        model = Project
        fields = ['title','image','description','tags','demo_link','source_link']

