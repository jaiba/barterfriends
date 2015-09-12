from django.shortcuts import render


def home(request):
    return render(request, 'barterfriends/index.html')


def about(request):
    return render(request, 'barterfriends/about.html')