from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout

# Create your views here.


def userAuth(request):
    if request.method == "POST":
        if request.POST['is_login'] == '1':
            username = request.POST['login_username']
            password = request.POST['login_password']
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return HttpResponse("Logged in")
            else:
                return HttpResponse("Invalid Credentials")
        else:
            username = request.POST['signup_username']
            password = request.POST['signup_password']
            password2 = request.POST['signup_password2']
            email = request.POST['signup_email']
            if password != password2:
                return HttpResponse("Passwords do not match")
            
            try:
                user = User.objects.create_user(username, email, password)
                user.save()
                return HttpResponse("Signed up")
            except:
                # print the exception
                return HttpResponse("Username already exists")
            
    return render(request, "auth.html")