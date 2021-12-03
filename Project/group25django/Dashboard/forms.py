from django import forms
from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.contrib.auth.models import User
from .models import index

class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username', 'email', 'password1', 'password2']

class storeForm(ModelForm):
    class Meta: 
        model = index
        fields = ('date', 'height', 'weight', 'calories', 'protein', 'fat', 'carbs')
        widgets = {
            'date' : forms.TextInput(attrs = {'class' : 'form-control'}),
            'height' : forms.TextInput(attrs = {'class' : 'form-control'}),
            'weight' : forms.TextInput(attrs = {'class' : 'form-control'}),
            'calories' : forms.TextInput(attrs = {'class' : 'form-control'}),
            'protein' : forms.TextInput(attrs = {'class' : 'form-control'}), 
            'fat' : forms.TextInput(attrs = {'class' : 'form-control'}), 
            'carbs': forms.TextInput(attrs = {'class' : 'form-control'})
        }