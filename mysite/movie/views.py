from django.shortcuts import render
from django.shortcuts import redirect

# Create your views here.

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