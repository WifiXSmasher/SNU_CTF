from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

class Projects(models.Model):
    PROJECT_TYPES = [
        ('Ong', 'Ongoing'),
        ('Com', 'Completed'),
    ]

    name = models.CharField(max_length=50)
    image = models.ImageField(upload_to='Projects/')
    date = models.DateTimeField(default=timezone.now)
    type = models.CharField(max_length=3, choices=PROJECT_TYPES)
    description = models.TextField(default= '')


    def __str__(self):
        return self.name
    