from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login as auth_login,logout
from django.contrib.auth.decorators import login_required
from .models import Message

def home(request):
    return render( request,"home.html")
    # return HttpResponse("all is okay")



def about(request):
    return render(request, "about.html")

def classes(request):
    return render(request, "classes.html")

def gallery(request):
    return render(request, "gallery.html")

def contact(request):
    if request.method == 'POST':
        username=request.POST.get('username')
        email=request.POST.get('email')
        msg=request.POST.get('msg')

        m=Message()
        m.name=username
        m.mail=email
        m.msg=msg
        
        m.save()
        return redirect('home')
    
    return render(request, "contact.html")

def login(request):
    if request.method == 'POST':
        username1=request.POST.get('username')
        password1=request.POST.get('pass')
        user=authenticate(request, username=username1, password=password1)
        if user is not None:
            auth_login(request, user)
            return redirect('home')
        else:
            return HttpResponse("Username or Password in incorrect!!")
    return render(request, "login.html")

def signup(request):
    if request.method == 'POST': 
        username=request.POST.get('uname')
        
        email=request.POST.get('email')
        password=request.POST.get('pass1')
        password2=request.POST.get('pass2')


        if password != password2:
            return HttpResponse("Your password and confirm are not same!! ")
        
        else:
            my_user=User.objects.create_user(username, email, password)
            my_user.save()
            return redirect('login')
    return render(request, "signup.html")