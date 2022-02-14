from django.urls import path
from . import views

app_name='users'
urlpatterns = [
    path('',views.profiles,name='profiles-all'),
    path('profile/<str:pk>/',views.profile,name='single-profile'),
    path('login/',views.loginUser,name='login'),
    path('logout/',views.logoutUser,name='logout'),
    path('register/',views.registerUser,name='register'),
    path('account/',views.userAccount,name='account'),
    path('edit-account/',views.editAccount,name='edit-account'),
]