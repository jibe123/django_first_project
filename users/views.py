from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import login as login_, authenticate, logout as logout_
from .forms import AuthForm

# Create your views here.

def login(request):
    if request.user.is_authenticated:
        return redirect('/posts/')
    else:
        if request.method == 'GET':
            form = AuthForm()
        else:
            form = AuthForm(request.POST)
            if form.is_valid():
                user = authenticate(
                    request,
                    username=form.cleaned_data['username'],
                    password=form.cleaned_data['password'],
                )

                if user:
                    login_(request, user)
                else:
                    form.add_error('username', 'Данные для входа неверные')

        return render(request, 'users/login.html', {'form': form})


def logout(request):
    logout_(request)
    return redirect('/login/')

