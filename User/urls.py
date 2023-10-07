from django.urls import path
from .views import *

urlpatterns = [
    path('', userAuth, name='userAuth')
]