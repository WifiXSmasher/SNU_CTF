from django.db import models
from django.urls import reverse  # used for creating URLs to CTF detail pages
from django.contrib.auth.models import User


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
    # image = models.ImageField(upload_to='ctf_images/', blank=True, null=True)
    image = models.URLField(blank=True, null=True)   #for supabase storage


    # 7. Description of the CTF challenge
    description = models.TextField()

    # 8. Date of the CTF (can be when it's hosted or added)
    date = models.DateField()

    #points associates to the challange
    points = models.IntegerField()

    #optional files that the user can download 
    # challange_files = models.FileField(upload_to='ctf_files/', blank=True, null=True)
    challange_files = models.URLField(blank=True, null=True)#for supabase 
   

    solution = models.TextField(max_length = 50)

    # 9. Display the CTF's title as string representation in Django admin or shell
    def __str__(self):
        return self.title

    # 10. Return URL to this CTF's detail page using reverse lookup
    def get_absolute_url(self):
        return reverse('ctf_detail', args=[self.type.lower(), self.id])

    def get_absolute_detail_url(self):
        return reverse('ctf_detail', args=[self.type.lower(), self.title])
    
    
    
    # OVERRIDDEN save() method to upload files to Supabase buckets
    def save(self, *args, **kwargs):
        # Handle image upload
        if hasattr(self, '_image_file') and self._image_file:
            content = self._image_file.read()
            path = f"ctf-images/{self._image_file.name}"
            mime_type = mimetypes.guess_type(self._image_file.name)[0] or "application/octet-stream"
            supabase.storage.from_("ctf-images").upload(path, content, {"content-type": mime_type})
            self.image = supabase.storage.from_("ctf-images").get_public_url(path)

        # Handle challenge file upload
        if hasattr(self, '_challenge_file') and self._challenge_file:
            content = self._challenge_file.read()
            path = f"ctf-files/{self._challenge_file.name}"
            mime_type = mimetypes.guess_type(self._challenge_file.name)[0] or "application/octet-stream"
            supabase.storage.from_("ctf-files").upload(path, content, {"content-type": mime_type})
            self.challange_files = supabase.storage.from_("ctf-files").get_public_url(path)

        # Call original save method
        super().save(*args, **kwargs)



class UserCTFProgress(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    ctf = models.ForeignKey(CTFs, on_delete=models.CASCADE)
    points_awarded = models.PositiveIntegerField(default=0)
    solved_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('user', 'ctf')  # Prevent multiple entries per user/ctf