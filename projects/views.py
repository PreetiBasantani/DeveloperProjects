from datetime import datetime
from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import Project,Review,Tag
from .forms import ProjectForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages

# Create your views here.

projectsList = [
    {
        'id': '1',
        'title': 'Ecommerce Website',
        'description': 'Fully functional ecommerce website'
    },
    {
        'id': '2',
        'title': 'Portfolio Website',
        'description': 'A personal website to write articles and display work'
    },
    {
        'id': '3',
        'title': 'Social Network',
        'description': 'An open source project built by the community'
    }
]


def projects(request):
    # d_val = datetime.now()
    # context = { 'proj_list' : projectsList,
    #             'number' : 10, 
    #             'date_val':  d_val,
    #              }
    project_list = Project.objects.all()
    context = {'projects':project_list}


    return render(request,'proj/projects.html',context)

def project(request,pk):
    proj = None
    proj = Project.objects.get(id=pk)
    # for p_dict in projectsList:
    #     if p_dict['id'] == pk:
    #         proj_dict = p_dict
     
    context ={'proj' : proj,}
    return render(request,'proj/single-project.html',context)


@login_required(login_url='users:login')
def createProject(request):
    profile = request.user.profile
    form  = ProjectForm()

    if request.method == 'POST':
        form = ProjectForm(request.POST,request.FILES)
        if form.is_valid():
            project = form.save(commit=False)
            project.owner = profile
            project.save()
            messages.success(request,'Project created Successfully')
            return redirect('users:account')
        else:
            messages.error(request,'Some errror occurred')

    context = {'form':form}
    return render(request,'proj/project-form.html',context)

@login_required(login_url='users:login')
def updateProject(request,pk):
    proj = Project.objects.get(id=pk)
    proj_form =ProjectForm(instance =proj)
    
    if request.method == 'POST':
        proj_form = ProjectForm(request.POST,request.FILES, instance =proj)
        
        if proj_form.is_valid():
            proj_form.save()
            print('Image saved in database')
            return redirect('projects:projects')

    context = {'form':proj_form}
    return render(request,'proj/project-form.html',context)

@login_required(login_url='users:login')
def deleteProject(request,pk):
    proj = Project.objects.get(id=pk)

    if request.method == 'POST':
        
        proj.delete()
        return redirect('projects:projects')

    context ={'project' : proj}

    return render(request,'proj/delete-project.html',context)