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
from django.views.decorators.csrf import csrf_exempt
from django.http.response import JsonResponse, HttpResponse
from .models import Favourite, Comment
import json
from django.core import serializers


def show_post(request, post_id):
    return render(request, "mysite/post.html")


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
            # cm_json = {'username': cm.author.username, 'date_time': str(cm.date_time), 'text': cm.text,
            # 'avatar_url': cm.author.avatar.url}
            # print(cm_json)
            # cm_json = serializers.serialize('json', [cm], fields=('date_time', 'text', 'author.username'))
            # print(cm_json)
            # cm_json[0].avatar_url = cm.author.avatar.url
            # cm_json[0].nickname = cm.author.nickname
            # print(cm_json)
            list = [{'username': cm.author.username, 'date_time': str(cm.date_time), 'text': cm.text,
                     'avatar_url': cm.author.avatar.url}]
            print("%%%%%%%%%%%%%%%%5")
            print(cm.author.avatar.url)
            cm_json = json.dumps(list)
            return JsonResponse(dict(status='ok', comment=cm_json, comments_num=len(cms)))
        except:
            return JsonResponse({'status': 'false', 'text': cm.text, 'comments_num': len(cms)})


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
            new_post.save()
            messages.success(request, 'Post has been sent successfully!')
            return redirect("/movieprofile/" + movie.name)
        else:
            messages.error(request, 'Post has not been sent!')
            return redirect("/movieprofile/" + movie.name)
    else:
        return redirect('')