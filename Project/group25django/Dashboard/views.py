from django.shortcuts import render
from .models import User, Macro

# Create your views here.


def userMacros(request):
    macros = Macro.objects.all()
    return render(request, 'index.html', {'userMacros': macros})
