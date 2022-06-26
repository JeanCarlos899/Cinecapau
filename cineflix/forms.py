from django import forms 
from .models import *
  
class MovieForm(forms.ModelForm): 
  
    class Meta: 
        model = Movie 
        fields = ['name', 'genre', 'duration', 'description', 'poster'] 