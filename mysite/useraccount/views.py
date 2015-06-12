from django.shortcuts import render
from django.contrib.auth import authenticate
from django.contrib.auth import login as a_login
from django.contrib.auth import logout as a_logout
from django.shortcuts import redirect
from django.shortcuts import HttpResponse
from django.contrib.auth.hashers import *
from django.contrib.auth.decorators import login_required
from django.template import RequestContext, loader
from django.contrib import messages

# import models
from .models import UserProfile

# import forms
from .forms import RegisterForm

# Create your views here.


@login_required(login_url='/signin')
def activation(request):
    user = UserProfile.objects.get(id=request.user.id)
    if user.activation_code == request.REQUEST.get('activation'):
        user.is_activate = True
    return redirect("/home")


def register(request):
    print("hi")
    if request.method == "POST":
        print(request.POST)
        form = RegisterForm(request.POST)
        print(form)
        if form.is_valid():
            user = UserProfile.objects.create_user(form.cleaned_data['username'], form.cleaned_data['email'],
                                                   form.cleaned_data['password'])
            user.birth_date = form.cleaned_data['birth_date']
            user.nickname = form.cleaned_data['username']
            user.activation_code = "1"
            # user.activation_code = hashlib.sha224(user.username + user.password).hexdigest()
            # send_mail('Simorgh Hotel Reservation', "127.0.0.1:8000/activation/?activation=" + user.activation_code,
            #           '', [user.email],
            #           fail_silently=False)
            user.save()
            return redirect("/home")
        else:
            print("not valid")
            form = RegisterForm()
            return render(request, "mysite/mainpage.html")
    else:
        form = RegisterForm()
        return render(request, "mysite/mainpage.html")


def login(request):
    print(request.user.id)
    if request.method == "POST":
        username = request.POST.get("UserName", "")
        password = request.POST.get("password", "")
        user = authenticate(username=username, password=password)
        if user is not None:
            a_login(request, user)
            return render(request, 'mysite/home.html')
        else:
            return redirect('/', alert=True)


@login_required(login_url='')
def logout(request):
    if request.method == "GET":
        a_logout(request)
        messages.error(request, 'Username or password is incorrect!')
        return redirect('/')


def homepage(request):
    return render(request, "mysite/home.html")


def show_profile(request, username):
    return render(request, "mysite/profile.html")
