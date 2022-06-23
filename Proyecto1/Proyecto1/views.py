from cgitb import html
from datetime import datetime
from django.http import HttpResponse

def saludo(request):  # Primera vista
    doc = """
    <html>
        <body>
            <h1>
            Hola alumnos esta es nuestra primera petición de pag en Django
            </h1>
        </body>
    </html>
    """
    return HttpResponse(doc)

def despedida(request):  # Primera vista
    return HttpResponse("Hasta luego alumnos de Django")

def dameFecha(request):
    fecha_actual = datetime
