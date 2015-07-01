from django.core.serializers import json
from django.http import JsonResponse, HttpResponse
from django.shortcuts import render
from django.shortcuts import redirect
from django.core import serializers

# Create your views here.
from django.views.decorators.csrf import csrf_exempt

from .models import Movie
from post.models import Post
from useraccount.models import UserProfile


def show_movie(request, movie_name):
    try:
        movie = Movie.objects.get(name=movie_name)
        rates = Post.objects.filter(movie=movie).values_list('rate', flat=True)
        if len(rates):
            rate = sum(rates) / len(rates)
        else:
            rate = ''
        if request.user.is_authenticated():
            user = UserProfile.objects.get(id=request.user.id)
        else:
            user = None
    except Movie.DoesNotExist:
        movie = None
    prev_post = Post.objects.filter(movie=movie, author=user)
    user_rate = None
    if len(prev_post) == 1:
        user_rate = prev_post[0].rate
    can_post = user and (len(prev_post) == 0)
    print(can_post)
    if movie is not None:
        return render(request, "mysite/movieProfile.html",
                      {'user': user, 'movie': movie, 'rate': rate, 'can_post': can_post, 'user_rate': user_rate})
    else:
        return redirect('/mainpage')


def mainpage(request):
    return redirect('/mainpage')


@csrf_exempt
def suggestion(request, number):
    if request.method == 'POST':
        user = UserProfile.objects.get(id=request.user.id)

        all_movies = Movie.objects.all()
        movies = []
        for movie in all_movies:
            if len(Post.objects.filter(author=user, movie=movie)) != 0:
                continue
            movies.append(movie)
            if len(movies) == 3:
                break
        new_list = [serializers.serialize('json', [o]) for o in movies]
        return JsonResponse(dict(status=True, Movies=new_list))