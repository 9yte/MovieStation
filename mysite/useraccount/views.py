from django.shortcuts import render
from django.contrib.auth import authenticate
from django.contrib.auth import login as a_login
from django.contrib.auth import logout as a_logout
from django.shortcuts import redirect
from django.shortcuts import HttpResponse
from django.contrib.auth.hashers import *
from django.contrib.auth.decorators import login_required
from django.template import RequestContext, loader
from django.contrib import messages
from django.http.response import HttpResponse, JsonResponse

# import models
from django.views.decorators.csrf import csrf_exempt
from .models import UserProfile
from post.models import Post
from datetime import datetime, date

# import forms
from .forms import RegisterForm

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
        form = RegisterForm(request.POST)
        print(form)
        if form.is_valid():
            user = UserProfile.objects.create_user(form.cleaned_data['username'], form.cleaned_data['email'],
                                                   form.cleaned_data['password'])
            user.birth_date = form.cleaned_data['birth_date']
            user.nickname = form.cleaned_data['username']
            user.activation_code = "1"
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
    print(request.user.id)
    if request.method == "POST":
        username = request.POST.get("UserName", "")
        password = request.POST.get("password", "")
        user = authenticate(username=username, password=password)
        if user is not None:
            print("User accepted")
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
def homepage(request):
    user = UserProfile.objects.get(id=request.user.id)
    followings = user.followings.all()
    posts = []
    for f in followings:
        user_posts = Post.objects.filter(author=f)
        posts += user_posts
    posts += Post.objects.filter(author=user)
    posts.sort(key=lambda x: x.date_time, reverse=True)
    return render(request, "mysite/home.html", {"posts": posts})


@login_required(login_url='/')
def show_profile(request, username):
    nowUser = UserProfile.objects.get(id=request.user.id)
    try:
        user = UserProfile.objects.get(username=username)
    except:
        user = None
    if user is not None:
        posts = Post.objects.filter(author=user)
        if user.username == nowUser.username:
            return render(request, "mysite/profile.html",
                          {"user": nowUser, "owner": True, "other": user, "posts": posts})
        else:
            if user in nowUser.followings.all():
                return render(request, "mysite/profile.html",
                              {"user": nowUser, "owner": False, "follows": True, "other": user, "posts": posts})
            else:
                return render(request, "mysite/profile.html",
                              {"user": nowUser, "owner": False, "follows": False, "other": user, "posts": posts})
    else:
        # TODO error page
        return HttpResponse("Error : cant find requsted user")


@csrf_exempt
def follow(request):
    if request.method == 'POST':
        currentUser = UserProfile.objects.get(id=request.user.id)
        username = request.POST.get('followed')
        user = UserProfile.objects.get(username=username)
        currentUser.followings.add(user)
        user.followers.add(currentUser)
        currentUser.save()
        user.save()
        return JsonResponse({'status': 'ok'})


@csrf_exempt
def edit(request):
    if request.method == 'POST':
        nickname = request.POST.get('nickname')
        email = request.POST.get('email')
        birth_date = request.POST.get('birth_date')
        birth_date = datetime.strptime(birth_date, "%B %d, %Y")
        birth_date = birth_date.strftime("%Y-%m-%d")
        user = UserProfile.objects.get(id=request.user.id)
        UserProfile.objects.filter(id=request.user.id).update(nickname=nickname, email=email, birth_date=birth_date)
        return JsonResponse({'status': 'ok'})

@csrf_exempt
def unfollow(request):
    if request.method == 'POST':
        currentUser = UserProfile.objects.get(id=request.user.id)
        username = request.POST.get('followed', '')
        user = UserProfile.objects.get(username=username)
        currentUser.followings.remove(user)
        user.followers.remove(currentUser)
        currentUser.save()
        user.save()
        return JsonResponse({'status': 'ok'})