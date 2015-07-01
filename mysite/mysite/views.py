from django.shortcuts import render


def mainpage(request):
    print("mainpage")
    return render(request, "mysite/mainpage.html")


def show_searchResult(request):
    return render(request, "mysite/search.html");