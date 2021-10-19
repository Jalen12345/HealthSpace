from django.shortcuts import render

# Create your views here.

# return the home page
def home(request):
    return render(request, 'index.html')