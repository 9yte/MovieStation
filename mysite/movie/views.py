from django.shortcuts import render
from django.shortcuts import redirect

# Create your views here.

from .models import Movie


def show_movie(request, movie_id):
    try:
        movie = Movie.objects.get(id=movie_id)
        rate = 8
    except Movie.DoesNotExist:
        movie = None
    if movie is not None:
        return render(request, "mysite/movieProfile.html", {'movie': movie, 'rate': rate})
    else:
        return redirect('/mainpage')


def mainpage(request):
    return redirect('/mainpage')