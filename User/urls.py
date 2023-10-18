from django.urls import path
from .views import *

urlpatterns = [
    path('', userAuth, name='userAuth'),
    path('logout/', userLogout, name='userLogout'),
    path('profile/', myProfile, name='myProfile'),
]