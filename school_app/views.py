from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login as auth_login,logout
from django.contrib.auth.decorators import login_required
from .models import Message, Gallery

def home(request):
    return render( request,"home.html")
    # return HttpResponse("all is okay")



def about(request):
    return render(request, "about.html")

def classes(request):
    return render(request, "classes.html")


def gallery(request):
    images = Gallery.objects.all()
    return render(request, 'gallery.html', {'images': images})



login_required(login_url='login',redirect_field_name='login')
def contact(request):
    if request.method == 'POST':
        if request.user.is_authenticated:
            msg = request.POST.get('msg')
            username = request.user.username
            email = request.user.email

            m = Message(name=username, mail=email, msg=msg)
            m.save()
            return redirect('home')
        else:
            return HttpResponse("Please log in to send a message.")
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



def user_logout(request):
    logout(request)
    return redirect('home')