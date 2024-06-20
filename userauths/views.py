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
            try:
                
                new_user = form.save(commit=False)  # Don't save the user yet
                new_user.email_verified = False
                new_user.save()

                fullname = form.cleaned_data.get("full_name")
                
                new_user = authenticate(username=form.cleaned_data['email'],
                                        password=form.cleaned_data['password']
                )
                login(request, new_user)
       
                return render(request,"core/index.html",{'message': f"Account created successfully"})
            
            except IntegrityError as e:
               
                form.add_error('email', 'This email address is already in use.')
        
        errors = form.errors.as_json()
        return JsonResponse(request,"user/register.html",{'errors': errors})

    return render(request, "user/register.html")

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
                return redirect("core:home")
            else:
                
                return redirect("userauths:sign-in")
        except User.DoesNotExist:
           
            return redirect("userauths:sign-in")


    return render(request, "user/login.html")


def account_view(request):
    return render(request, "core/playlist.html")


def logout_view(request):
    logout(request)
    return redirect("core:home")




