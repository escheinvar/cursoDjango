from telnetlib import Telnet
from django.shortcuts import render
from django.views.generic import TemplateView, ListView, CreateView

from .models import MyBase
from .forms import MyForma

# Create your views here.
class MyClase(TemplateView):
    template_name = 'home/MyPagina.html'


class MyClase2(TemplateView):
    template_name = 'MyPaginita.html'

class MyClase3(ListView):
    template_name = 'MyPaginita.html'
    model = MyBase
    context_object_name = 'lista_prueba'

class PruebaCreateView(CreateView):
    template_name = "home/add.html"
    model = MyBase
    #fields = ['titulo','subtitulo','cantidad']
    success_url = '.'
    form_class = MyForma