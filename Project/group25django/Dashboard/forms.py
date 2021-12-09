from django import forms
from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm, UsernameField
from django import forms
from django.contrib.auth.models import User
from django.forms.forms import Form
from .models import index, Sleep

class CreateUserForm(UserCreationForm):
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput(attrs={'class':'input', 'type': 'password'}))
    password2 = forms.CharField(label= 'Confirm Password', widget=forms.PasswordInput(attrs={'class':'input', 'type': 'password'}))
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username', 'email', 'password1', 'password2']
        widgets = {}
        for i in range(len(fields) - 2):
            widgets[fields[i]] = forms.TextInput(attrs={
                'class': 'input',
                'type': 'text'
            })
class LoginForm(forms.Form):
    username = forms.CharField(label='Username', widget=forms.TextInput(attrs={'class':'input', 'type': 'text'}))
    password = forms.CharField(label='Password', widget=forms.PasswordInput(attrs={'class':'input', 'type': 'password'}))
    def get_Username(self):
        return self.cleaned_data['username']
    def get_Password(self):
        return self.cleaned_data['password']

class storeForm(ModelForm):
    class Meta: 
        model = index
        fields = ['date', 'height', 'weight', 'calories', 'protein', 'fat', 'carbs']
        widgets = {
            'date': forms.DateInput(
                format=('%Y-%m-%d'),
                attrs={
                    'class': 'input',
                    'type': 'date'
              }),
        }
        for i in range(len(fields) - 1):
            widgets[fields[i+1]]= forms.TextInput(
                  attrs={
                      'class': 'input',
                      'type': 'number',
                  }
              ) 
class sleepForm(ModelForm):
    class Meta:
        model = Sleep
        fields = ['date', 'sleepHours', 'wakeUp', 'quality']
        widgets = {
            'date': forms.DateInput(
                format=('%Y-%m-%d'),
                attrs={'class': 'input', 
                    'placeholder': 'Select a date',
                    'type': 'date'
              }),
              'wakeUp': forms.TimeInput(
                  format='%H:%M',
                  attrs={
                      'class': 'input',
                      'type': 'time'
                  }
              ),
              'sleepHours': forms.TextInput(
                  attrs={
                      'class': 'input',
                      'type': 'number',
                  }
              ),
              'quality': forms.Select(
                  attrs={
                    'class': 'input'
                  }
              )
        }