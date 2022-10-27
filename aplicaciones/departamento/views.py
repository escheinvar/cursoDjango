from typing import List
from django.shortcuts import render
from django.views.generic import ListView

from .models import Departamento

# Create your views here.
class VerDepto(ListView):
    template_name = 'departamento/verDepto.html'
    model = Departamento
    context_object_name = 'Deptos'


