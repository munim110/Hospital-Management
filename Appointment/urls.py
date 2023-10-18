from django.urls import path
from .views import *


urlpatterns = [
    path('create_appointment_slots/', create_appointment_slots, name="create_appointment_slots"),
    path('book_appointment/', book_appointment, name="book_appointment"),
    path('profile/<int:doctor_id>/', doctor_profile, name='doctor_profile'),
    path('book_appointment/<int:appointment_id>/', book_appointment_slot, name='book_appointment')
]