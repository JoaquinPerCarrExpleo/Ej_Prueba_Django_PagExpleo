#from django.contrib import admin
from django.urls import path
#from . import views
from .views import home, form, getSearch, delete#, modi

urlpatterns = [
    #path('indexhtml/', views.home),
    path('', home),
    path('forms/', form),
    path('search/', getSearch),
    path('borrar/', delete),
    #path('mod/', modi),
]