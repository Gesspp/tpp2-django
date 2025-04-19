from django.shortcuts import render, redirect
from .forms import UserRegisterForm
from django.contrib.auth import login

def signup(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')
    else:
        form = UserRegisterForm()
    return render(request, 'signup.html', {'form': form})

def profile(request):
    return render(request, 'profile.html')