from email import contentmanager
from django import forms

class createService (forms.Form):
    title = forms.CharField(label="Titulo", max_length=200)
    content = forms.CharField(label="Contenido", max_length=200)
    fechaIni = forms.DateField(label="Fecha creación servicio")
    
    
class SearchService (forms.Form):
    title = forms.CharField(label="Titulo", max_length=200, min_length=1)

    