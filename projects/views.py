from django.shortcuts import render
from .models import Projects
from django.shortcuts import get_object_or_404


# Create your views here.
def my_projects(request):

    projects = Projects.objects.all()
    return render(request, 'projects/my_projects.html', {'Projects':projects})


def project_details(request,project_id):
    project = get_object_or_404(Projects, pk= project_id)#project will go to the db and fetch shit  
    return  render(request,'projects/project_detail.html',{'project' : project})#this name should be the same as the above return object 
