from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def add_prescription(request):
    if request.method == 'POST':
        print(request.POST)
        return HttpResponse('Prescription added successfully')
    return render(request, 'Prescription/add_prescription.html')
