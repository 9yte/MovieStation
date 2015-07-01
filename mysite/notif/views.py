from django.http import JsonResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from .models import Notif
from useraccount.models import UserProfile
from django.core import serializers

@csrf_exempt
def getNotif(request):
    print('getNotif')
    if request.method == 'POST':
        user = UserProfile.objects.filter(id=request.user.id)
        notifs = Notif.objects.filter(user=user).order_by('-date_time')[:6]
        new_notifs = [serializers.serialize('json', [o]) for o in notifs]

        return JsonResponse(dict(status=True, notifs=new_notifs))

    return JsonResponse(dict(status=False))