from django.shortcuts import render
from django.contrib.auth import authenticate
from django.contrib.auth import login as a_login
from django.contrib.auth import logout as a_logout
from django.shortcuts import redirect
from django.shortcuts import HttpResponse
from django.contrib.auth.hashers import *
from django.contrib.auth.decorators import login_required

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
        form = RegisterForm(request.POST)
        print(form)
        if form.is_valid():
            user = UserProfile.objects.create_user(form.cleaned_data['username'], form.cleaned_data['email'],
                                                   form.cleaned_data['password'])
            user.first_name = form.cleaned_data['first_name']
            user.last_name = form.cleaned_data['last_name']
            user.birth_date = form.cleaned_data['birth_date']
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
