from django.db import models

# Create your models here.
class CTFs(models.Model):
    CTF_TYPE = [
        ('STG', 'Stegnography'),
        ('WEB', 'Web Security'),
        ('NET', 'Networks'),
        ('PVE', 'Privilage Escalation'),
        ('ENM', 'Enumeration'),
    ]
    title = models.CharField(max_length=100)
    type = models.CharField(max_length=3, choices=CTF_TYPE)
    image= models.ImageField(upload_to='ctf_images/', blank=True, null=True)
    description = models.TextField()
    date = models.DateField()

    def __str__(self):
        return self.title