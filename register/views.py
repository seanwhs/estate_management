from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
from . forms import MyUserCreationForm
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.forms import AuthenticationForm
from django.shortcuts import redirect
from django.db import IntegrityError

# Create your views here.

def register(request):
    context = {
        "form":MyUserCreationForm, 
        "password_mismatch_error":"Passwords Do NoT Match!!",
        "duplicate_username": "Username taken. Use another user name!",
        }
    if request.method == 'GET':
        return render(request, 'register/register.html', context)
    else:
        if request.POST['password1'] == request.POST['password2']:
            try:
                user = User.objects.create_user(
                    request.POST['username'],
                    password = request.POST['password1'],
                )
                user.save()
                login(request, user)
                return redirect('landing')
            except IntegrityError:
                context = {
                    "error": "Duplicate User Name", 
                    "error_message":"User name is  taken. Choose another name!"
                    }
                return render(request, 'register/error.html', context)
        else: 
            context = {
                "error": "Password Mismatch" , 
                "error_message":"Passwords DO NOT MATCH!"
                }

            return render(request, 'register/error.html', context)

def logout_user(request):
    logout(request)
    return redirect('landing')

def login_user(request):
    if request.user.is_authenticated:
        return redirect("landing")
    if request.method == 'GET':
        return render(request, 'register/login_user.html', {'form':AuthenticationForm})
    else:
        user = authenticate(
                request,
                username=request.POST['username'],
                password=request.POST['password']
                ) 
    if user is None:
        location = "'login_user'"
        context = {
            'error': 'Name and password mismatch',
            'error_message': 'Username and password mismatch. Try again.',
        }
        return render(request,'register/error.html', context) 
            
    else: 
        login(request,user)
        return redirect('landing')


