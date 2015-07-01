from django.shortcuts import render
from django.shortcuts import redirect
from useraccount.forms import RegisterForm
from useraccount.models import UserProfile



def mainpage(request):
    u = UserProfile.objects.filter(id=request.user.id)
    if len(u) == 0:
        form = RegisterForm()
        next_url = request.GET.get('next', None)
        return render(request, "mysite/mainpage.html", {'form': form, 'next': next_url})
    else:
        return redirect("/home")