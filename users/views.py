
from django.shortcuts import render,redirect
from .models import Profile
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from .forms import CustomUserCreationForm,ProfileForm


# Create your views here.
def profiles(request):
    profiles = Profile.objects.all()
    context = {
        'profiles':profiles,
    }
    return render(request,'users/profiles.html',context)


def profile(request,pk):
    profile = Profile.objects.get(id = pk)
    topskills = profile.skill_set.exclude(description = "")
    otherskills= profile.skill_set.filter(description ="")
    context = {
         'profile':profile,
         'topskills':topskills,
         'otherskills':otherskills,
    }
    return render(request,'users/single-profile.html',context)


def loginUser(request):
    page='login'
    if request.method == 'POST':
        username= request.POST['username']
        password = request.POST['password']

        try:
            user = User.objects.get(username=username)
        except:
            messages.error(request,'User is not available')
        
        user = authenticate(request,username=username,password=password)
        
        if user is not None:
            login(request,user)
            return redirect('users:profiles-all')
        else:
            messages.error(request,"username and password doesn't match")

    context={'page':page}
    return render(request,'users/login_register.html',context)



def logoutUser(request):
    logout(request)
    messages.info(request,'USer successfully logged out')
    return redirect('users:login')


def registerUser(request):
    page='register'
    form = CustomUserCreationForm()


    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.username = user.username.lower()
            user.save()
            messages.success(request,'User successfully created')
            
            return redirect('users:login')
        else:
            messages.error(request,'some error occurred')

    context={
        'page':page,
        'form':form,
    }


    return render(request,'users/login_register.html',context)


def userAccount(request):
    profile = request.user.profile
    context={
        'profile':profile,
    }
    return render(request,'users/account.html',context)


def editAccount(request):
    profile = request.user.profile
    form = ProfileForm(instance=profile)

    if request.method == 'POST':
        form = ProfileForm(request.POST,request.FILES,instance=profile)
        if form.is_valid():
            form.save()
            messages.success(request,'Profile updated Successfully')
            return redirect('users:account')
        else:
            messages.error(request,'Enter valid data in fields')   

    context={'form':form}
    return render(request,'users/profile-form.html',context)

