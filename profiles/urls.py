from django.urls import path
from . import views

urlpatterns = [
    path('', views.profile_landing, name='profile_landing'),  #for /profiles
]
