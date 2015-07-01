from django.core import serializers

__author__ = 'hojjat'
from django.shortcuts import render
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required
from .forms import PostForm
from .models import Post
from useraccount.models import UserProfile
from movie.models import Movie
from django.contrib import messages
from datetime import datetime
from django.utils import timezone
from django.views.decorators.csrf import csrf_exempt
from django.http.response import JsonResponse, HttpResponse
from .models import Favourite, Comment
import json


@login_required(login_url='')
def show_post(request, post_id):
    user = UserProfile.objects.get(id=request.user.id)
    posts = Post.objects.filter(id=post_id)
    if len(posts) == 1:
        final_posts = []
        followings = user.follow.all()
        if posts[0].author in followings or posts[0].author == user:
            for post in posts:
                x = len(Favourite.objects.filter(post=post))
                cms = Comment.objects.filter(post=post)
                post.likes = x
                post.comments = cms
                post.comments_num = len(cms)
                post.liked = (len(Favourite.objects.filter(post=post, user=user)) == 1)
                final_posts.append(post)
            return render(request, "mysite/post.html",
                          {'posts': final_posts, 'user': user})
    return redirect("/home")


@csrf_exempt
@login_required(login_url='')
def like(request, post_id):
    if request.method == 'POST':
        try:
            p = Post.objects.get(id=post_id)
            user = UserProfile.objects.get(id=request.user.id)
            l = Favourite.objects.filter(user=user, post=p)
            req = request.POST.get('req')
            if req == '0' and len(l) == 0:  # if the user wants to like a post that didn't like it before!
                print(3)
                fav = Favourite.objects.create(post=p, user=user, date_time=datetime.now())
                fav.save()
                l = Favourite.objects.filter(post=p)
                return JsonResponse({'status': 'like', 'likes': len(l)})
            elif req == '1' and len(l) == 1:  # if the user wants to unlike a post that like it before!
                fav = Favourite.objects.get(post=p, user=user)
                fav.delete()
                l = Favourite.objects.filter(post=p)
                return JsonResponse({'status': 'unlike', 'likes': len(l)})
        except:
            return JsonResponse({'status': 'wrong request'})


@csrf_exempt
@login_required(login_url='')
def comment(request, post_id):
    if request.method == 'POST':
        try:
            p = Post.objects.get(id=post_id)
            user = UserProfile.objects.get(id=request.user.id)
            text = request.POST.get('text')
            cm = Comment.objects.create(author=user, post=p, text=text, date_time=datetime.now())
            cm.save()
            cms = Comment.objects.filter(post=p)
            list = [{'username': cm.author.username, 'date_time': str(cm.date_time.strftime("%B %d, %Y, %I:%M %p")),
                     'text': cm.text,
                     'avatar_url': cm.author.avatar.url}]
            print(cm.author.avatar.url)
            cm_json = json.dumps(list)
            return JsonResponse(dict(status='ok', comment=cm_json, comments_num=len(cms)))
        except:
            return JsonResponse({'status': 'false', 'text': cm.text, 'comments_num': len(cms)})


@csrf_exempt
@login_required(login_url='')
def get_post(request):
    if request.method == "POST":
        num = int(request.POST.get("num"))
        last_date = request.POST.get("last_date")
        query = request.POST.get("query", None)
        user_id = request.POST.get("user_id", None)
        user = UserProfile.objects.get(id=request.user.id)
        followings = user.follow.all()
        posts = []
        print(last_date)
        if last_date[-1] == '.':
            last_date = last_date[0:len(last_date) - 3] + 'm'
        print(last_date)
        try:
            last_date = datetime.strptime(last_date, "%B %d, %Y, %I:%M %p")
        except:
            last_date = datetime.strptime(last_date, "%B %d, %Y, %I %p")
        if query is not None:
            for f in followings:
                user_posts = Post.objects.filter(author=f, date_time__lt=last_date, text__contains=query)
                posts += user_posts
            posts += Post.objects.filter(author=user, date_time__lt=last_date, text_contains=query)
        elif user_id is not None:
            posts += Post.objects.filter(author=user, date_time__lt=last_date)
        else:
            for f in followings:
                user_posts = Post.objects.filter(author=f, date_time__lt=last_date)
                posts += user_posts
            user_posts = Post.objects.filter(author=user, date_time__lt=last_date)
            posts += user_posts
        posts.sort(key=lambda x: x.date_time, reverse=True)
        counter = 0
        final_posts = []
        final_comments = []
        for p in posts:
            if counter >= num:
                break
            x = len(Favourite.objects.filter(post=p))
            cms = Comment.objects.filter(post=p)
            f = {'likes': x, 'username': p.author.username, 'nickname': p.author.nickname,
                 'avatar_url': p.author.avatar.url,
                 'text': p.text, 'rate': p.rate, 'date_time': str(p.date_time.strftime("%B %d, %Y, %I:%M %p")),
                 'id': p.id,
                 'description': p.movie.description,
                 'movie_url': p.movie.cover_photo.url,
                 'movie_name': p.movie.name, 'comments_num': len(cms),
                 'liked': (len(Favourite.objects.filter(post=p, user=user)) == 1)}
            final_posts.append(f)
            for cm in cms:
                c = {'text': cm.text, 'date_time': str(cm.date_time.strftime("%B %d, %Y, %I:%M %p")),
                     'avatar_url': cm.author.avatar.url,
                     'username': cm.author.username, 'nickname': cm.author.nickname}
                final_comments.append(c)
            counter += 1
        final_comments = json.dumps(final_comments)
        final_posts = json.dumps(final_posts)
        return JsonResponse(dict(status='ok', posts=final_posts, comments=final_comments, username=user.username,
                                 avatar_url=user.avatar.url))


@login_required(login_url='')
def post(request, movie_id):
    print("hi")
    if request.method == "POST":
        author = UserProfile.objects.get(id=request.user.id)
        movie = Movie.objects.get(id=movie_id)
        prev_post = Post.objects.filter(movie=movie, author=author)
        if len(prev_post) == 1:
            messages.error(request, 'You post about this film before!')
            return redirect("/movieprofile/" + movie.name)
        form = PostForm(request.POST)
        print(form)
        if form.is_valid():
            new_post = Post.objects.create(author=author, movie=movie, rate=form.cleaned_data['rate'],
                                           text=form.cleaned_data['text'],
                                           date_time=datetime.now())
            current_rate = movie.rate
            number_of_voters = movie.rate_numbers
            if number_of_voters == 0:
                new_rate = form.cleaned_data['rate']
            else:
                new_rate = current_rate * number_of_voters + form.cleaned_data['rate']
                new_rate /= (number_of_voters + 1)
            movie.rate = new_rate
            movie.rate_numbers = number_of_voters + 1
            movie.save()
            new_post.save()
            messages.success(request, 'Post has been sent successfully!')
            return redirect("/movieprofile/" + movie.name)
        else:
            messages.error(request, 'Post has not been sent!')
            return redirect("/movieprofile/" + movie.name)
    else:
        return redirect('')

@csrf_exempt
def getNotif(request):
    print('GetNotif req')
    if request.method == 'POST':
        user = UserProfile.objects.get(id=request.user.id)
        print('from ')
        print(user.username)
        comments = Comment.objects.filter(post__author__username=user.username).order_by('-date_time')[:4]
        comment_owners = [o.author for o in comments]
        print('comments founded')
        print(comments)
        likes = Favourite.objects.filter(post__author__username=user.username).order_by('-date_time')[:4]
        like_owners = [o.user for o in likes]
        print('likes founded')
        print(likes)

        new_comments = [serializers.serialize('json', [o]) for o in comments]
        new_comment_owners = [serializers.serialize('json', [o]) for o in comment_owners]
        new_likes = [serializers.serialize('json', [o]) for o in likes]
        new_like_owners = [serializers.serialize('json', [o]) for o in like_owners]

        return JsonResponse(dict(status=True, notif_comments=new_comments, cm_owners=new_comment_owners,
                                 notif_likes=new_likes, like_owners=new_like_owners))

    return JsonResponse(dict(status=False))