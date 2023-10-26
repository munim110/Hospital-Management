from django.db import models
from User.models import Patient, Doctor

# Create your models here.
class MedicineDose(models.Model):
    medicine_name = models.CharField(max_length=100)
    dose = models.CharField(max_length=100)
    days = models.CharField(max_length=100)

class Test(models.Model):
    test_name = models.CharField(max_length=100)
    specification = models.CharField(max_length=100)


class Prescription(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    date = models.DateField(auto_now_add=True)
    symptoms = models.TextField()
    diagnosis = models.TextField()
    medicines = models.ManyToManyField(MedicineDose)
    tests = models.ManyToManyField(Test)
    advice = models.TextField()
