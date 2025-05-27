from django.shortcuts import render, redirect
from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required



# @login_required(login_url='/profiles/profile.html')
# def profile_view(request):
#     return render(request, 'profiles/profile.html', {'user': request.user})
# User = get_user_model()

def profile_landing(request):
    if request.user.is_authenticated:
        return render(request, "profiles/profile_landing.html", {"user": request.user})
    else:
        return render(request, "profiles/guest_profile.html")

