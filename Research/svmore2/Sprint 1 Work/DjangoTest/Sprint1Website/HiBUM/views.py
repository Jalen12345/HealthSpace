from django.shortcuts import render
from django.http import HttpResponse

#where you make the views from the urls pcal
def home(request):
  #return an HTTP Response of hello world
  return render(request, 'index.html')

