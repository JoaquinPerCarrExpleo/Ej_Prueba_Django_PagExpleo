from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from app.forms import SearchService, createService
from app.models import servicios

def home(response):
    result = servicios.objects.get(id="1")
    return render(response, "index.html", {"x":result}) # Como un diccionario clave: valor

def form(response):
    if response.method == "POST":
        form = createService(response.POST)
        
        if form.is_valid():
            a = form.cleaned_data["title"]
            b = form.cleaned_data["content"]
            c = form.cleaned_data["fechaIni"]
            res = servicios.objects.get(id="1")
            res.item_set.create(title=a, content=b, fechaIni=c)
            res.save()
        return HttpResponseRedirect("/") 
    else:
        form = createService()  # Le pasas una lista de valores vacia a la BBDD     
    return render(response, "form.html", {"pepito":form})


def getSearch(response):
    if response.method == "GET":
        form = SearchService(response.GET)
        if form.is_valid():
            a = form.cleaned_data["title"]
            res = servicios.objects.get(id="1")
            res.item_set.get(title=a)
            print(res)
            def busqueda(response):
               return HttpResponseRedirect(response, "busqueda.html", {"consulta":res}) 
        
    else:
        form = SearchService() 
        print("Generamos el get para llenarlo y realizar la consulta")      
    return render(response, "get.html", {"menganito":form})

