__author__ = 'hojjat'
from django.shortcuts import render
# from django.shortcuts import redirect
# from django.shortcuts import HttpResponse


def homepage(request):
    return render(request, "mysite/home.html")


def show_profile(request):
    return render(request, "mysite/profile.html")