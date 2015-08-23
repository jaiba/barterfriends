from django.shortcuts import render, redirect
from .forms import UserRegister


def home(request):
    return render(request, 'barterfriends/index.html')


def about(request):
    return render(request, 'barterfriends/about.html')


def register(request):
    if request.method == 'POST':
        form = UserRegister(data=request.POST)
        if form.is_valid():
            form.save(commit=True)
            return redirect('/')
    else:
        form = UserRegister()
        return render(request, 'registration/register.html', {'form': form})
