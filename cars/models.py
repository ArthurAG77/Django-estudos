from django.db import models

# Create your models here.
class Car(models.Model):
    id = models.AutoField(primary_key=True)
    model = models.CharField(max_length=200, blank=True, null=True)
    brand = models.CharField(max_length=100, blank=True, null=True)
