from django.shortcuts import render
from django.contrib.auth import authenticate
from django.contrib.auth import login as a_login
from django.contrib.auth import logout as a_logout
import re
from django.shortcuts import redirect
from django.shortcuts import HttpResponse
from django.contrib.auth.hashers import *
from django.contrib.auth.decorators import login_required
from django.template import RequestContext, loader
from django.contrib import messages
from django.http.response import HttpResponse, JsonResponse

# import models
from django.views.decorators.csrf import csrf_exempt
from .models import UserProfile, Follow

from post.models import Comment, Favourite
from post.models import Post
from datetime import datetime
from django.core import serializers

# import forms
from .forms import RegisterForm, ChangePassForm, EditForm

# Create your views here.


@login_required(login_url='/signin')
def activation(request):
    user = UserProfile.objects.get(id=request.user.id)
    if user.activation_code == request.REQUEST.get('activation'):
        user.is_activate = True
    return redirect("/home")


def register(request):
    print("hi")
    if request.method == "POST":
        print(request.POST)
        form = RegisterForm(request.POST, request.FILES)
        print(form)
        if form.is_valid():
            user = UserProfile.objects.create_user(form.cleaned_data['username'], form.cleaned_data['email'],
                                                   form.cleaned_data['password'])
            user.birth_date = form.cleaned_data['birth_date']
            user.nickname = form.cleaned_data['username']
            user.activation_code = "1"
            user.avatar = form.cleaned_data['avatar']
            # user.activation_code = hashlib.sha224(user.username + user.password).hexdigest()
            # send_mail('Simorgh Hotel Reservation', "127.0.0.1:8000/activation/?activation=" + user.activation_code,
            # '', [user.email],
            # fail_silently=False)
            user.save()
            return redirect("/home")
        else:
            print("not valid")
            form = RegisterForm()
            return render(request, "mysite/mainpage.html")
    else:
        form = RegisterForm()
        return render(request, "mysite/mainpage.html")


def login(request):
    if request.method == "POST":
        username = request.POST.get("UserName", "")
        password = request.POST.get("password", "")

        user = authenticate(username=username, password=password)
        if user is not None:
            a_login(request, user)
            return redirect('/home')
        else:
            messages.error(request, 'Username or password is incorrect!')
            return redirect('/')


@login_required(login_url='/')
def logout(request):
    if request.method == "GET":
        a_logout(request)
        return redirect('/')


@login_required(login_url='/')
def homepage(request, number_of_posts=10):
    user = UserProfile.objects.get(id=request.user.id)
    followings = user.follow.all()
    posts = []
    for f in followings:
        user_posts = Post.objects.filter(author=f)
        posts += user_posts
    posts += Post.objects.filter(author=user)
    posts.sort(key=lambda x: x.date_time, reverse=True)
    counter = 0
    final_posts = []
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
    return render(request, "mysite/home.html", {"posts": final_posts})


@login_required(login_url='/')
def show_profile(request, username):
    nowUser = UserProfile.objects.get(id=request.user.id)
    try:
        user = UserProfile.objects.get(username=username)
    except:
        user = None
    if user is not None:
        #print(user.username)
        #print('followings')
        #for user2 in user.follow.all():
        #    print(user2.username)
        #print('followers')
        #for user2 in user.followed_by.all():
        #    print(user2.username)

        posts = Post.objects.filter(author=user)
        followers = UserProfile.objects.filter(follow=user)
        if user.username == nowUser.username:
            return render(request, "mysite/profile.html",
                          {"user": nowUser, "owner": True, "other": user, "posts": posts, "followers": followers})
        else:
            if user in nowUser.follow.all():
                return render(request, "mysite/profile.html",
                              {"user": nowUser, "owner": False, "follows": True, "other": user, "posts": posts
                                  , "followers": followers})
            else:
                return render(request, "mysite/profile.html",
                              {"user": nowUser, "owner": False, "follows": False, "other": user, "posts": posts
                                  , "followers": followers})
    else:
        # TODO error page
        return HttpResponse("Error : cant find requsted user")


@csrf_exempt
def change_password(request):
    if request.method == 'POST':
        form = ChangePassForm(request.POST)
        if form.is_valid():
            current_pass = form.cleaned_data['current_password']
            password = form.cleaned_data['password']
            user = UserProfile.objects.get(id=request.user.id)
            if check_password(current_pass, user.password):
                UserProfile.objects.filter(id=request.user.id).update(password=make_password(
                    password, salt=None, hasher='default'))
                # send_mail('Simorgh Hotel Reservation', 'your password has been changed.',
                # '', [user.email],
                #                   fail_silently=False)
                return JsonResponse({'status': 3})
            else:
                return JsonResponse({'status': 1})
        else:
            return JsonResponse({'status': 2})


@csrf_exempt
def follow(request):
    if request.method == 'POST':
        currentUser = UserProfile.objects.get(id=request.user.id)
        username = request.POST.get('followed')
        user = UserProfile.objects.get(username=username)
        #currentUser.follow.add(user)
        Follow.objects.create(follower=currentUser, followed=user)
        print(currentUser.username)
        print("folows")
        print(user.username)
        #user.followers.add(currentUser)
        #currentUser.save()
        #user.save()
        return JsonResponse({'status': 'ok'})


@csrf_exempt
def edit(request):
    if request.method == 'POST':
        form = EditForm(request.POST, request.FILES)
        if form.is_valid():
            nickname = form.cleaned_data["nickname"]
            email = form.cleaned_data["email"]
            avatar = form.cleaned_data["avatar"]
            birth_date = request.POST.get('birth_date')
            if re.search(r',', birth_date):
                try:
                    birth_date = datetime.strptime(birth_date, "%B %d, %Y")
                except:
                    birth_date = datetime.strptime(birth_date, "%b. %d, %Y")
                birth_date = birth_date.strftime("%Y-%m-%d")
            user = UserProfile.objects.get(id=request.user.id)
            if avatar is not None:
                user.avatar = avatar
            user.birth_date = birth_date
            user.nickname = nickname
            user.email = email
            user.save()
            return JsonResponse({'status': 'ok', 'url': user.avatar.url})


@csrf_exempt
def unfollow(request):
    if request.method == 'POST':
        currentUser = UserProfile.objects.get(id=request.user.id)
        username = request.POST.get('followed', '')
        user = UserProfile.objects.get(username=username)
        #currentUser.follow.remove(user)
        Follow.objects.remove(follower=currentUser, followed=user)
        #user.followers.remove(currentUser)
        #currentUser.save()
        #user.save()
        return JsonResponse({'status': 'ok'})


@csrf_exempt
def suggest(request, number):
    if request.method == 'POST':
        Current_User = UserProfile.objects.get(id=request.user.id)
        all_user = UserProfile.objects.all()[:10]
        users = []
        for user in all_user:
            if len(Current_User.follow.filter(id=user.id)) != 0:
                continue
            users.append(user)
            if len(users) == 3:
                break
        new_list = [serializers.serialize('json', [o]) for o in users]
        return JsonResponse(dict(status=True, Peoples=new_list))

