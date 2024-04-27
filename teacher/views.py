from django.contrib import messages
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout

from children.models import Child


@login_required
def home(request):
    return render(request, 'teacher.html')


def logins(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            if Child.objects.filter(child=user).exists():
                return redirect('children')
            return redirect('home')
        messages.error(request, 'Логин же пароль туура эмес')
    return render(request, 'login.html')


def logouts(request):
    logout(request)
    return redirect('login')
