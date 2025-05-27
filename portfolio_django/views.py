from django.http import HttpResponse 
from django.shortcuts import render

def home(request):
    return render(request,'website/index.html')

def My_projects(request):
    return render(request, 'projects/my_projects.html')

def CTFs(request):
    return render(request, 'ctfs/ctfs.html')

