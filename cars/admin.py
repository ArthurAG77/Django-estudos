from django.contrib import admin
from cars.models import Car, Brand

# Register your models here.

class BrandAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name', )

class CarAdmin(admin.ModelAdmin):
    list_display = ('model', 'brand', 'factory_year', 'model_year', 'value') # Campos que você quer que apareça no django admin
    search_fields = ('model', 'brand') # Em quais campos a pesquisa deve funcionar?

admin.site.register(Car, CarAdmin)
admin.site.register(Brand, BrandAdmin)