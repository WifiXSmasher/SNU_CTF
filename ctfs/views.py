from django.shortcuts import render
from .models import CTFs
from django.shortcuts import get_object_or_404

# shows all ctf categories on /ctfs page
def ctf_list(request):
    ctftypes = CTFs.CTF_TYPE  # gets all predefined ctf types from model
    return render(request, 'ctfs/ctfs.html', {'ctftypes': ctftypes})  # sends it to template

# shows all ctfs of a specific type
def ctf_type(request, type):
    type_upper = type.upper()  # converts url type to uppercase for matching
    ctf_type_dict = dict(CTFs.CTF_TYPE)  # makes a dict from model choices

    if type_upper not in ctf_type_dict:
        raise Http404("CTF category not found")  # if type is invalid, return 404

    ctfs = CTFs.objects.filter(type=type_upper)  # gets all ctfs of this type
    return render(request, 'ctfs/ctf_type.html', {
        'ctfs': ctfs,
        'type': ctf_type_dict[type_upper]  # sends human-readable type name
    })


def ctf_detail(request, type, title):
    type_upper = type.upper()
    ctf = get_object_or_404(CTFs, type=type_upper, title=title)
    return render(request, 'ctfs/ctf_details.html', {'ctf': ctf})