from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Patient(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    blood_group = models.CharField(max_length=3, blank=True, null=True)
    age = models.IntegerField(blank=True, null=True)

    def __str__(self) -> str:
        return self.user.username



class Doctor(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    qualification = models.CharField(max_length=100)
    contact_number = models.CharField(max_length=20)
    
    def __str__(self) -> str:
        return self.user.username

