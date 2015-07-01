from django.shortcuts import render
from django.shortcuts import redirect
from useraccount.forms import RegisterForm
from useraccount.models import UserProfile



def mainpage(request):
    u = UserProfile.objects.filter(id=request.user.id)
    if len(u) == 0:
        form = RegisterForm()
        return render(request, "mysite/mainpage.html", {'form': form})
    else:
        return redirect("/home")
