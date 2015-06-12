__author__ = 'hojjat'
from django.shortcuts import render
from django.shortcuts import redirect
# from django.shortcuts import HttpResponse


def show_post(request):
    return render(request, "mysite/post.html")
