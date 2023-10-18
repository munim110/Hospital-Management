from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from .models import Doctor, Patient
from Appointment.models import Appointment_slots

# Create your views here.


def userAuth(request):
    if request.method == "POST":
        if request.POST['is_login'] == '1':
            username = request.POST['login_username']
            password = request.POST['login_password']
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('home')
            else:
                return HttpResponse("Invalid Credentials")
        else:
            username = request.POST['signup_username']
            password = request.POST['signup_password']
            password2 = request.POST['signup_password2']
            first_name = request.POST['signup_first_name']
            last_name = request.POST['signup_last_name']
            email = request.POST['signup_email']
            if password != password2:
                return HttpResponse("Passwords do not match")
            
            try:
                user = User.objects.create_user(username, email, password)
                user.first_name = first_name
                user.last_name = last_name
                user.save()
                patient = Patient.objects.create(user=user)
                patient.save()
                return redirect('userAuth')
            except:
                # print the exception
                return HttpResponse("Username already exists")
            
    return render(request, "auth.html")


def userLogout(request):
    logout(request)
    return redirect('userAuth')


def myProfile(request):
    if not request.user.is_authenticated:
        return redirect('userAuth')
    user = request.user
    try:
        doctor = Doctor.objects.get(user=user)
        return redirect('create_appointment_slots')
    except:
        patient = Patient.objects.get(user=user)
        appointments = Appointment_slots.objects.filter(patient=patient)
        return render(request, "patient/patient_profile.html", {'patient': patient, 'appointments': appointments})