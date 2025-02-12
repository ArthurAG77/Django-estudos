from django.shortcuts import render

# Create your views here.

def carview(request):
    return render(request,'cars/cars.html') 