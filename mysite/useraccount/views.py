from django.shortcuts import render

# Create your views here.

@login_required(login_url='/signin')
def activation(request):
    print request.user.id
    user = UserProfile.objects.get(id=request.user.id)
    if user.activation_code == request.REQUEST.get('activation'):
        print "hi"
        Group.objects.get(name='simple_users').user_set.add(user)
    return redirect("/home")