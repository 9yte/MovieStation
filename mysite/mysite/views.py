__author__ = 'hojjat'
from django.shortcuts import render
from django.shortcuts import redirect


def mainpage(request):
    print("mainpage")
    return render(request, "mysite/mainpage.html")