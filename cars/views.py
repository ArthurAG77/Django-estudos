from django.shortcuts import render

# Create your views here.

def carview(request):
    return render(request,'cars/cars.html')  # em settings.py o diretório de templates é BASE_DIR/templates então ele não enxerga diretamente o arquivo html, por isso adicionamos o nome do diretório antes do html