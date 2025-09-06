from django import forms
from .models import item

class FichaForm(forms.ModelForm):
    class Meta:
        model = item
        fields = ['name', 'description', 'image']
