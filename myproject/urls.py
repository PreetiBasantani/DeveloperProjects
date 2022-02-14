from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

app_name = 'myproject'

urlpatterns = [
    path('',views.projects,name='projects'),
    path('project/<str:pk>/',views.project,name='project'),   #str variable can be passed as paramter to function
    path('create-project/',views.createProject,name = 'create-project'),
    path('delete-project/<str:pk>/',views.deleteProject,name = 'delete-project'),
    path('update-project/<str:pk>/',views.updateProject,name = 'update-project'),

]


urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT )
