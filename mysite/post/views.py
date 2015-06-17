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
# from django.shortcuts import HttpResponse


def show_post(request):
    return render(request, "mysite/post.html")


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