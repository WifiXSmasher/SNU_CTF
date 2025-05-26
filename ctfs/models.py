from django.db import models
from django.urls import reverse  # used for creating URLs to CTF detail pages

class CTFs(models.Model):
    # 1. Hardcoded types for CTFs (example: Steganography, Web Security, etc.)
    CTF_TYPE = [
        ('STG', 'Steganography'),
        ('WEB', 'Web Security'),
        ('NET', 'Networks'),
        ('PVE', 'Privilege Escalation'),
        ('ENM', 'Enumeration'),
    ]

    # 2. Hardcoded categories — this is the new addition
    CATEGORIES = [
        ('BAS', 'Beginner'),        # BAS = Beginner
        ('INT', 'Intermediate'),    # INT = Intermediate
        ('ADV', 'Advanced'),        # ADV = Advanced
    ]

    # 3. Title of the CTF
    title = models.CharField(max_length=100)

    # 4. Type of the CTF using hardcoded choices from CTF_TYPE
    type = models.CharField(max_length=3, choices=CTF_TYPE)

    # 5. New: Category of the CTF, using predefined CATEGORIES. Default is 'BAS' (Beginner)
    category = models.CharField(max_length=3, choices=CATEGORIES, default='BAS')

    # 6. Optional image for the CTF challenge
    image = models.ImageField(upload_to='ctf_images/', blank=True, null=True)

    # 7. Description of the CTF challenge
    description = models.TextField()

    # 8. Date of the CTF (can be when it's hosted or added)
    date = models.DateField()

    # 9. Display the CTF's title as string representation in Django admin or shell
    def __str__(self):
        return self.title

    # 10. Return URL to this CTF's detail page using reverse lookup
    def get_absolute_url(self):
        return reverse('ctf_detail', args=[self.type.lower(), self.id])

    def get_absolute_detail_url(self):
        return reverse('ctf_detail', args=[self.type.lower(), self.title])
