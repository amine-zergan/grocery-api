
from django.contrib import admin
from django.core.exceptions import ValidationError
 
from .models import Category
from django.forms import ModelForm
 
 
class CategoryForm(ModelForm):
   def clean(self):
       background = self.cleaned_data['background']
       
       if not background.startswith("#"):
           raise ValidationError("couleur doit etre en hexdecimal")
       else:
           return self.cleaned_data