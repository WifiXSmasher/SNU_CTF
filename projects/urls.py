from django.urls import path, include
from . import views


#localhost:8000/projects
urlpatterns = [
        path('', views.my_projects,name='all_projects'),
        path('my_projects/', views.my_projects, name='my_projects'),
        path('<int:project_id>/', views.project_details,name='project_details'),
        
]
