from django.shortcuts import render
from django.http.response import JsonResponse
from useraccount.models import UserProfile
import json
from post.models import Post
from django.db.models import Q
from movie.models import Movie
# Create your views here.


def search(request):
    if request.method == "GET":
        query = request.GET.get("search")
        users = UserProfile.objects.filter(username__contains=query)
        l = [x.username for x in users]
        return JsonResponse({'search': json.dumps(l)})


def search_result(request):
    if request.method == "GET":
        query = request.GET.get("query")
        users = UserProfile.objects.filter(Q(username__contains=query) | Q(email__contains=query))
        posts = Post.objects.filter(text__contains=query)
        movies = Movie.objects.filter(Q(name__contains=query) | Q(description__contains=query))
        return render(request, "mysite/search.html", {'users': users, 'posts': posts, 'movies': movies, 'query': query})