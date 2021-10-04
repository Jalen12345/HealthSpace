from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def home(request):
    #return HttpResponse("Dear god, please work")
    new_User = User(userID=123,FirstName="Eren",LastName="Yeager",Goals="Gain Weight",New="True")
    new_User.save()
    return render(request, 'index.html',{'name':'BUMstead'})
    