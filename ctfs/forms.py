# Update your forms.py

from django import forms
from .models import Comments


class Comments_form(forms.ModelForm):
    
    #inner class META
    class Meta:
        model = Comments
        fields = ['content']
        widgets = {
            'content': forms.Textarea(attrs={
                'placeholder': 'Any Thoughts...?',
                'rows': 3,
                'class': 'form-control'
            })
        }
      
