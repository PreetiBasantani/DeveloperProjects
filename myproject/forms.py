
from django.forms import ModelForm, widgets
from django import forms
from .models import Project

class ProjectForm(ModelForm):
    class Meta:
        model =  Project
        # fields = '__all__'
        fields = ['name','img','description','tags','vote_total','vote_ratio']
        widgets ={
            'tags': forms.CheckboxSelectMultiple(),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args,**kwargs)

        for label,field in self.fields.items():
            field.widget.attrs.update({'class': 'input input--text', 'placeholder':'Enter value'})

        # self.fields['name'].widget.attrs.update({'class':'input','placeholder':'Enter project name'})