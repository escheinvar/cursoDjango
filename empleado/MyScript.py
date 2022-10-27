from curses.ascii import HT
from django.http import HttpResponse

def Myfuncion(request):
    return HttpResponse('<B>Hola</b> Mundo')

