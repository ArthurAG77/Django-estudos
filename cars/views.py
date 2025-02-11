from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def CarView(request):
    return HttpResponse('<h1>Meus carros</h1>')