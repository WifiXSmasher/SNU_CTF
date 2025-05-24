from django.shortcuts import render
from .models import CTFs
# Create your views here.
def ctf_list(request):
    ctfs = CTFs.objects.all()
    return render(request, 'ctfs/ctfs.html', {'ctfs': ctfs})
