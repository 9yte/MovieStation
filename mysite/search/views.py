from django.shortcuts import render
from django.http.response import JsonResponse
from useraccount.models import UserProfile
import json
# Create your views here.


def search(request):
    if request.method == "GET":
        query = request.GET.get("search")
        users = UserProfile.objects.filter(username__contains=query)
        l = [x.username for x in users]
        print(l)
        return JsonResponse({'search': json.dumps(l)})