from django.forms import ModelForm, models
from  .models import Project
from django import forms

class ProjectForm(ModelForm):
    class Meta:
        model = Project
        fields = ['title','image','description','tags','demo_link','source_link']
        widgets={
            'tags':forms.CheckboxSelectMultiple(),
        }

    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)

        for label,field in self.fields.items():
            field.widget.attrs.update({'class':'input'})


        # self.fields['title'].widget.attrs.update({'class':'input'})

