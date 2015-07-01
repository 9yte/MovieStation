from django.shortcuts import render
from django.http.response import JsonResponse
from useraccount.models import UserProfile
import json
from post.models import Post
from django.db.models import Q
from movie.models import Movie
from post.models import Favourite, Comment
from django.contrib.auth.decorators import login_required
# Create your views here.


@login_required(login_url='/')
def search(request):
    if request.method == "GET":
        query = request.GET.get("search")
        users = UserProfile.objects.filter(username__contains=query).exclude(username="admin")
        l = [x.username for x in users]
        return JsonResponse({'search': json.dumps(l)})


@login_required(login_url='/')
def search_result(request, number_of_posts=2):
    if request.method == "GET":
        user = UserProfile.objects.get(id=request.user.id)
        query = request.GET.get("query")
        users = UserProfile.objects.filter(Q(username__contains=query)).exclude(
            username="admin")
        for u in users:
            if u in user.follow.all():
                print(u.username)
                u.follows = True
            else:
                u.follows = False
        posts = Post.objects.filter(text__contains=query).order_by('-date_time')
        final_posts = []
        counter = 0
        for post in posts:
            if counter >= number_of_posts:
                break
            x = len(Favourite.objects.filter(post=post))
            cms = Comment.objects.filter(post=post)
            post.likes = x
            post.comments = cms
            post.comments_num = len(cms)
            post.liked = (len(Favourite.objects.filter(post=post, user=user)) == 1)
            final_posts.append(post)
            counter += 1
        movies = Movie.objects.filter(Q(name__contains=query) | Q(description__contains=query))
        return render(request, "mysite/search.html",
                      {'users': users, 'posts': final_posts, 'movies': movies, 'query': query, 'is_scroll': True,
                       'num_of_posts': len(posts)})

