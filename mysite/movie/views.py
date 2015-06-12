from django.shortcuts import render
from django.shortcuts import redirect

# Create your views here.

from .models import Movie


def show_movie(request, movie_id):
    movie = Movie.objects.get(id=movie_id)
    if movie:
        return render(request, "mysite/movieProfile.html", {'id': movie_id})
    else:
        return redirect('/mainpage')