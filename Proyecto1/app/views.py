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


def getSearch(request):
    if request.method == "GET":
        form = SearchService(request.GET)
        if form.is_valid():
            a = form.cleaned_data["title"]
            print("Lo que le metemos al get: ", a)
            res = servicios.objects.get(id = "1")
            try:
                mostrar = res.item_set.get(title = a)
                print("Resultado del res: " , res.item_set.get(title=a))    
            except:
                mostrar = {"title": "No se ha encontrado coincidencias, por favor introduzca un título existente"}
            finally:
                form = SearchService()
                return render(request, "get.html", {"consulta":mostrar, "menganito":form})
            
    else:
        form = SearchService() 
        print("Generamos el get para llenarlo y realizar la consulta")      
    return render(request, "get.html", {"menganito":form})


def delete(response):
    if response.method == "POST":
        form = SearchService(response.POST)
        if form.is_valid():
            a = form.cleaned_data["title"]
            res = servicios.objects.get(id="1")
            try:
                elem_del = res.item_set.get(title = a)
                print("Vamos a eliminar el servicio: ", elem_del)
                elem_del.delete()
                mostrar = "Se ha elimininado este servicio de la BBDD"
            except:
                mostrar = "No se ha encontrado coincidencias, por favor elimine un servicio existente"
            finally:
                form = SearchService()
                return render(response, "borrar.html", {"respuesta": mostrar, "elim":form}) 
    else:
        form = SearchService()  # Le pasas una lista de valores vacia a la BBDD     
    return render(response, "borrar.html", {"elim":form})


# def modi(response):
#     if response.method == "PUT":
#         form = createService(response.POST)
#         if form.is_valid():
#             a = form.cleaned_data["title"]
#             b = form.cleaned_data["content"]
#             c = form.cleaned_data["fechaIni"]
#             res = servicios.objects.get(id="1")
#             res.item_set.create(title=a, content=b, fechaIni=c)
#             try:
#                 mostrar = res.item_set.get(title = a)
#                 print("Resultado del res: " , res.item_set.get(title=a))    
#             except:
#                 mostrar = {"title": "No se ha encontrado coincidencias, por favor introduzca un título existente"}
#             finally:
#                 form = createService()
#                 return render(response, "get.html", {"consulta":mostrar, "menganito":form})
            
#     else:
#         form = createService() 
#         print("Generamos el get para llenarlo y realizar la consulta")      
#     return render(response, "get.html", {"menganito":form})


