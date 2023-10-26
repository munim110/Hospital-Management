from django.urls import path
from .views import *

urlpatterns = [
    path('add_prescription/', add_prescription, name='add_prescription'),
]