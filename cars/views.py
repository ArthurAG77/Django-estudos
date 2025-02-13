from django.shortcuts import render
from cars.models import Car
# Create your views here.

def carview(request):
    cars = Car.objects.filter(brand__name__contains='fiat') # -> Seleciona todos os registros do banco de dados

    return render(
        request,'cars/cars.html',
        {'cars': cars}
        )  # em settings.py o diretório de templates é BASE_DIR/templates então ele não enxerga diretamente o arquivo html, por isso adicionamos o nome do diretório antes do html
