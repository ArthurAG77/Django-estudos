from django.contrib import admin
from cars.models import Car

# Register your models here.
class CarAdmin(admin.ModelAdmin):
    list_display = ('model', 'brand', 'factory_year', 'model_year', 'value') # Campos que você quer que apareça no django admin
    search_fields = ('model', 'brand' ) # Em quais campos a pesquisa deve funcionar?

admin.site.register(Car, CarAdmin)