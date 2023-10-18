from django.shortcuts import render, redirect
from datetime import datetime
from django.utils import timezone
from .models import *
from django.http import HttpResponse

# Create your views here.

def create_appointment_slots(request):
    if not request.user.is_authenticated:
        return redirect('userAuth')
    user = request.user
    try:
        doctor = Doctor.objects.get(user=user)
    except:
        return HttpResponse('You are not a doctor')

    if request.method == "POST":
        if request.POST.get('date2'):
            date = request.POST.get('date2')
            date = datetime.strptime(date, '%Y-%m-%d').date()
            start_time = datetime.combine(date, datetime.min.time())
            end_time = datetime.combine(date, datetime.max.time())
            start_time = timezone.make_aware(start_time)
            end_time = timezone.make_aware(end_time)

            appointments = Appointment_slots.objects.filter(doctor=doctor, start_time__gte=start_time, start_time__lte=end_time)
            return render(request, "appointment/create_appointment_slots.html", {'appointments': appointments})
        date = request.POST.get('date')
        if not date:
            return HttpResponse("Enter a date")
        date = datetime.strptime(date, '%Y-%m-%d').date()
        start_time = request.POST.get('start-time')
        if not start_time:
            return HttpResponse("Enter a start time")
        start_time = datetime.strptime(start_time, '%H:%M').time()
        end_time = request.POST.get('end-time')
        if not end_time:
            return HttpResponse("Enter an end time")
        end_time = datetime.strptime(end_time, '%H:%M').time()
        start = datetime.combine(date, start_time)
        end = datetime.combine(date, end_time)
        if start < datetime.now():
            return HttpResponse("Start time cannot be in the past")
        if start > end:
            return HttpResponse("Start time cannot be greater than end time")
        start_time = timezone.make_aware(start)
        end_time = timezone.make_aware(end)
        doctor = Doctor.objects.get(user=user)
        appointment = Appointment_slots.objects.create(start_time=start_time, end_time=end_time, doctor=doctor)
        appointment.save()
        return redirect('create_appointment_slots')
    return render(request, "appointment/create_appointment_slots.html")


def book_appointment(request):
    doctors = Doctor.objects.all()
    return render(request, "appointment/book_appointment.html", {'doctors': doctors})


def doctor_profile(request, doctor_id):
    if not request.user.is_authenticated:
        return redirect('userAuth')
    user = request.user
    try:
        patient = Patient.objects.get(user=user)
    except:
        return HttpResponse('You are not a patient')
    if request.method == "POST":
        date = request.POST.get('date')
        if not date:
            return HttpResponse("Enter a date")
        date = datetime.strptime(date, '%Y-%m-%d').date()
        start_time = datetime.combine(date, datetime.min.time())
        start_time = timezone.make_aware(start_time)
        end_time = datetime.combine(date, datetime.max.time())
        end_time = timezone.make_aware(end_time)
        doctor = Doctor.objects.get(id=doctor_id)
        appointments = Appointment_slots.objects.filter(doctor=doctor, start_time__gte=start_time, start_time__lte=end_time, is_available=True)
        if not appointments:
            return HttpResponse("No appointments available")
        return render(request, "doctor/profile.html", {'appointments': appointments, 'doctor': doctor})

    doctor = Doctor.objects.get(id=doctor_id)
    return render(request, "doctor/profile.html", {'doctor': doctor,})


def book_appointment_slot(request, appointment_id):
    if not request.user.is_authenticated:
        return redirect('userAuth')
    user = request.user
    try:
        patient = Patient.objects.get(user=user)
    except:
        return HttpResponse('You are not a patient')
    appointment = Appointment_slots.objects.get(id=appointment_id)
    appointment.is_available = False
    appointment.patient = patient
    appointment.save()
    return redirect('myProfile')