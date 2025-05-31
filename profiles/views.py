from django.shortcuts import render, redirect
from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required
from ctfs.models import UserCTFProgress
from django.db.models.functions import Coalesce
from django.db.models import Sum
from django.db.models import Value, IntegerField


# @login_required(login_url='/profiles/profile.html')
# def profile_view(request):
#     return render(request, 'profiles/profile.html', {'user': request.user})
# User = get_user_model()


def profile_landing(request):
    if request.user.is_authenticated:
        # calculate total points from solved CTFs
        total_points = (
            UserCTFProgress.objects
            .filter(user=request.user)
            .aggregate(points=Coalesce(Sum('points_awarded'), Value(0), output_field=IntegerField()))
        )['points']

        return render(request, "profiles/profile_landing.html", {
            "user": request.user,
            "total_points": total_points
        })
    else:
        return render(request, "profiles/guest_profile.html")
