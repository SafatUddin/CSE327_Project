from django.shortcuts import render
from .models import Car

def index(request):
    # Fetch all cars
    cars = Car.objects.all() 
    
    context = {
        'cars': cars
    }
    
    return render(request, 'listings/index.html', context)