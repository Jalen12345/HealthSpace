from django.shortcuts import render
from .models import User, Macro

# Create your views here.


def userMacros(request):
    macros = Macro.objects.all()
    return render(request, 'index.html', {'userMacros': macros})
# return the home pcal
def home(request):
    return render(request, 'index.html')
def dashboard(request):
    return render(request, 'dashboard.html')
def diet(request):
    return render(request, 'diet.html')
def exercise(request):
    return render(request, 'exercise.html')
def form(request):
    return render(request, 'form.html')
def login(request):
    return render(request, 'login.html')
def sleep(request):
    return render(request, 'sleep.html')
