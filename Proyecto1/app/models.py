from sqlite3 import Date
from turtle import title
from django.db import models

# Create your models here.
class servicios(models.Model):
    name= models.CharField(max_length=200)
    def __str__(self):
        return self.name
    
class Item(models.Model):
    serv = models.ForeignKey(servicios, on_delete=models.CASCADE)
    title = models.CharField(max_length=300)
    content = models.CharField(max_length=3000)
    fechaIni = models.DateField(default = Date.today)

    def __str__(self): #Funcion rara ;)
        return self.title

