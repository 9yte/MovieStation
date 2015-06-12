from django.shortcuts import render
from django.shortcuts import redirect

# Create your views here.

from .models import Movie


def show_movie(request, movie_id):
    try:
        movie = Movie.objects.get(id=movie_id)
    except Movie.DoesNotExist:
        movie = None
    if movie is not None:
        return render(request, "mysite/movieProfile.html", {'movie': movie})
    else:
        return redirect('/mainpage')


def mainpage(request):
    return redirect('/mainpage')