from django.shortcuts import render


def default(request):
    return render(request, "home.html")
