from django.shortcuts import render
from django.views.generic import (TemplateView, ListView, DetailView, CreateView, UpdateView, DeleteView)

#from aplicaciones.departamento.models import Departamento

# Create your views here.
from .models import Empleado

class Inicio(TemplateView):
    template_name = "inicio.html"

######################################### Pág. TodosEmpls. con buscador
class MyTodosEmpleados(ListView):
    template_name = "persona/TodosEmpls.html"
    #model = Empleado
    context_object_name = 'VerTodosEmpleados'
    paginate_by = 3
    context_object_name = 'empleados'

    def get_queryset(self):
        MyVar = self.request.GET.get("kword",'')
#        act = Empleado.activo
        MyLista = Empleado.objects.filter(
            full_name__icontains = MyVar.upper() #and act==1
        )
        return MyLista.filter(activo='0')


######################################## Pág. TodosEmpls. ADMIN con buscador 
class TodosEmpleadosAdmin(ListView):
    template_name = "persona/AdminTodos.html"
    context_object_name = 'AdminTodosEmpleados'
    #paginate_by = 3

    def get_queryset(self):
        MyVar = self.request.GET.get("buscarUR",'')
        MyLista = Empleado.objects.filter(
            departamento__shor_name__icontains = MyVar.upper()
        )
        return MyLista


######################################### Pág. AreaEmpls
class MyArea(ListView):
    template_name = "persona/Areaempls.html"
    def get_queryset(self):
        MyVar = self.kwargs['area']
        MyLista = Empleado.objects.filter( 
            departamento__shor_name = MyVar
        )
        return MyLista

######################################### Pág.Campo de búsqueda
class VistaBuscar(ListView):
    template_name = "persona/Buscar.html"
    context_object_name = 'Busqueda'
     
    def get_queryset(self):
        MyVar = self.request.GET.get("kword",'')
        MyLista = Empleado.objects.filter(
            departamento__shor_name = MyVar.upper()
        )
        return MyLista
        
        print ("*****\n")
        bla = self.request.GET.get("kword",'')
        print("===",bla)
        
######################################### Pág.many to many habilidades
class ListaHabilidades(ListView):
    template_name = "persona/habilidades.html"
    context_object_name = 'habilidades'
     
    def get_queryset(self):
        empleado = Empleado.objects.get(id='5')
        print ("===== ", empleado)
        return [empleado.habilidades.all(), empleado]


######################################### Generar DetailView
class VerDetalle(DetailView):
    model = Empleado
    template_name = "persona/detail.html"

    def get_context_data(self, **kwargs):
        context = super(VerDetalle, self).get_context_data(**kwargs)
        context['bla']= self
        context['ble']='Segunda variable'
        return context



######################################### CreateView
class CrearEmpleado(CreateView):
    template_name = "persona/crear.html"
    model = Empleado
    #fields =['first_name', 'last_name','job']
    fields =('__all__')
    success_url = '.'

    ### Validación:
    def form_valid(self, form):
        MyVar = form.save()
        MyVar.full_name = MyVar.first_name + '-' + MyVar.last_name
        MyVar.save()
        return super(CrearEmpleado, self).form_valid(form)


######################################## EditView
class EditarEmpleado(UpdateView):
    template_name = "persona/editar.html"
    model = Empleado
    fields=('__all__')
    success_url = '.'

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        print ("************** metodo post **************")
        return super().post(request, *args, **kwargs)

    ### Validación 
    def form_valid(self, form):
        print ("************** metodo form valid **************")
        MyVar = form.save()
        MyVar.full_name = MyVar.first_name + '-' + MyVar.last_name
        MyVar.save()
        return super(EditarEmpleado, self).form_valid(form)
    

################################################ DeleteView
class BorrarEmpleado(DeleteView):
    template_name = "persona/borrar.html"
    model = Empleado 