from django.shortcuts import render,redirect
from userauths.forms import UserRegisterForm
from django.contrib.auth import login, authenticate
from django.contrib import messages
from django.conf import settings
from django.contrib.auth import logout
from userauths.models import User
from django.http import JsonResponse, HttpResponse
from django.utils import timezone
from django.contrib.auth.hashers import make_password
from django.db import IntegrityError


def register_view(request):
    form = UserRegisterForm(request.POST)
    if request.method == "POST":
        if form.is_valid():
            new_user = form.save()
            messages.success(request, f"Account created successfully")
            new_user = authenticate(username=form.cleaned_data['email'],
                                    password=form.cleaned_data['password']
            )
            login(request, new_user)
            return redirect("core:home")
    context = {
        'form': form,
    }
    return render(request, 'user/register.html', context)


def login_view(request):
    if request.user.is_authenticated:
        return redirect("core:home")
    if request.method == "POST":
        email = request.POST.get('email')
        password = request.POST.get('password')

        try:
            user = User.objects.get(email=email)
            user = authenticate(request, email=email, password=password)
            if user is not None:
                login(request, user)
                
                messages.success(request, f"Successfully logged in.")
                return redirect("core:home")
            else:
                messages.warning(request, "User Doesn't Exist, create an account.")
        except:
            messages.warning(request, f"User with {email} does not exist")

    return render(request, 'user/login.html')


def account_view(request):
    return render(request, "core/playlist.html")


def logout_view(request):
    logout(request)
    return redirect("core:home")




