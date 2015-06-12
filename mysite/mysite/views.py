__author__ = 'hojjat'
from django.shortcuts import render
from django.shortcuts import redirect
# from django.shortcuts import HttpResponse


def mainpage(request):
    print("mainpage")
    return render(request, "mysite/mainpage.html")


def show_searchResult(request):
    return render(request, "mysite/search.html");