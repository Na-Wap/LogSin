from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required

@login_required(login_url='login')
def home(request):
    return render(request,'index.html')

def signup(request):
    error_message = None
    if request.method =='POST':
        uname=request.POST.get('username')
        email=request.POST.get('email')
        pass1=request.POST.get('password1')
        pass2=request.POST.get('password2')

        if pass1!=pass2:
              error_message = "Your password and confirm password doesnt match!!"
        else:
            my_user=User.objects.create_user(uname,email,pass1)
            my_user.save()
            return redirect('login')
    return render(request,'signup.html',{'error_message' : error_message})

def loginpage(request):
    error_message = None

    if request.method =='POST':
        uname=request.POST.get('username')
        pass1=request.POST.get('password')
        user=authenticate(request,username=uname,password=pass1)

        if user is not None:
            login(request,user)
            return redirect('index')
            
        else:
           error_message = "Your password or username id incorrect!!"


    return render(request,'login.html',{'error_message' : error_message})
# Create your views here.
