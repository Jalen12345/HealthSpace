from django.http.response import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import login
from django.http import HttpResponse
from Dashboard.models import User, Macro
from django.contrib import messages
from django.forms import inlineformset_factory
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login, logout
from .models import *
from .forms import CreateUserForm, storeForm, sleepForm, exerciseForm
from django.http import HttpResponseRedirect
# Create your views here.


def userMacros(request):
    if not request.user.is_authenticated:
        return HttpResponseRedirect('/login/')
    macros = Macro.objects.all()
    return render(request, 'dashboard.html', {'userMacros': macros})
# return the home pcal


def home(request):
    if not request.user.is_authenticated:
        return HttpResponseRedirect('/login/')
    return render(request, 'dashboard.html')


def dashboard(request):
    if request.method == "POST":
        print("test")
    if not request.user.is_authenticated:
        return HttpResponseRedirect('/login/')
    return render(request, 'dashboard.html')


def diet(request):
    if not request.user.is_authenticated:
        return HttpResponseRedirect('/login/')
    submitted = False
    if request.method == "POST":
        form = storeForm(request.POST)
        if form.is_valid():
            diet = form.save(commit=False)
            diet.user = request.user
            diet.save()
            return HttpResponseRedirect('/diet/')
    else:
        form = storeForm
        if 'submitted' in request.GET:
            submitted = True
    return render(request, 'diet.html', {"form": form, "submitted": submitted})


def exercise(request):
    if not request.user.is_authenticated:
        return HttpResponseRedirect('/login/')
    submitted = False
    if request.method == "POST":
        form = exerciseForm(request.POST)
        if form.is_valid():
            exercisef = form.save(commit=False)
            exercisef.user = request.user
            exercisef.save()
            return HttpResponseRedirect('/exercise/')
    else:
        form = exerciseForm
        if 'submitted' in request.GET:
            submitted = True
    all = Exercise.objects.all()
    return render(request, 'exercise.html', {"form": form, "submitted": submitted})


def form(request):
    if not request.user.is_authenticated:
        return HttpResponseRedirect('/login/')
    return render(request, 'form.html')


def loginPage(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return HttpResponseRedirect('/dashboard/')
        else:
            messages.info(request, 'username or password is incorrect')
    context = {}
    return render(request, 'login.html', context)


def logoutUser(request):
    logout(request)
    return HttpResponseRedirect('/login/')


def register(request):
    form = CreateUserForm()
    if(request.method == 'POST'):
        form = CreateUserForm(request.POST)
        if(form.is_valid()):
            form.save()
            messages.success(request, 'Account Successfully Created!')
            return HttpResponseRedirect('/login/')
    context = {'form': form}
    return render(request, 'register.html', context)


def sleep(request):
    if not request.user.is_authenticated:
        return HttpResponseRedirect('/login/')
    submitted = False
    if request.method == "POST":
        form = sleepForm(request.POST)
        if form.is_valid():
            sleep = form.save(commit=False)
            sleep.user = request.user
            sleep.save()
            return HttpResponseRedirect('/sleep/')
    else:
        form = sleepForm
        if 'submitted' in request.GET:
            submitted = True

    return render(request, 'sleep.html', {"form": form, "submitted": submitted})


def store(request):
    submitted = False
    if request.method == "POST":
        form = storeForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/store/')
    else:
        form = storeForm
        if 'submitted' in request.GET:
            submitted = True

    return render(request, 'store.html', {"form": form, "submitted": submitted})


def data(request):
    all_data = index.objects.all()
    return render(request, 'data.html', {'all': all_data})
