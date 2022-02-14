from datetime import datetime
import re
from django.shortcuts import redirect, render
from django.http import HttpResponse
from .forms import ProjectForm
from .models import Project,Review,Tag  

# Create your views here.
# projectsList = [
#     {
#         'id': '1',
#         'title': 'Ecommerce Website',
#         'description': 'Fully functional ecommerce website'
#     },
#     {
#         'id': '2',
#         'title': 'Portfolio Website',
#         'description': 'A personal website to write articles and display work'
#     },
#     {
#         'id': '3',
#         'title': 'Social Network',
#         'description': 'An open source project built by the community'
#     },
    
# ]


def projects(request):
    # return HttpResponse('List of Projects.')
    # today = datetime.today()
    # context ={  
    #            'projects' : projectsList,
    #            'number' : 10,
    #            'message' : 'This is Projects Template',
    #            'dateproj' : today,
    #            'proj' : ['E-commerce','Chat-Application','Shopping-Website'],
    # }
               
    project_list = Project.objects.all()
    context = {'projects':project_list}

    return render(request,'projects/projects.html', context)


def project(request,pk):
    # return HttpResponse('Single Project ' + str(pk))
    # single_proj = None
    # for i in projectsList:
    #     if i['id'] == pk:
    #          single_proj = i
    
    # context = {'project' : single_proj}

    proj = None
    proj = Project.objects.get(id=pk)     
    context ={'proj' : proj,}

    return render(request,'projects/single-project.html',context)


def createProject(request):
    form  = ProjectForm()

    if request.method == 'POST':
        form = ProjectForm(request.POST,request.FILES) 
        if form.is_valid():
            form.save()
            print('saved data')
            return redirect('myproject:projects')

    context = {'form':form}
    return render(request,'projects/project-form.html',context)

   

def deleteProject(request,pk):
    p = Project.objects.get(id=pk)
    msg = ''
    

    if request.method =='POST':
        p.delete()
        msg ='Project Deleted'
        # return redirect('myproject:projects')

    context={'project':p,
             'msg':msg,
            }
    return render(request,'projects/delete-form.html',context)


def updateProject(request,pk):
    p = Project.objects.get(id= pk)
    form = ProjectForm(instance=p)
    msg = ''

    if request.method == 'POST':
        form = ProjectForm(request.POST,instance=p)
        if form.is_valid():
            form.save()
            msg = 'Updated Successfully'
        return redirect('myproject:projects')

    context = {'form':form,
                'msg':msg,}

    return render(request,'projects/project-form.html',context)