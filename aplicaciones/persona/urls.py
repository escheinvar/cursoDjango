from django.urls import path
from . import views
## ursl de la App home
app_name ="persona_app"

urlpatterns = [
    path('', views.Inicio.as_view()),
    path('TodosEmpleados/', views.MyTodosEmpleados.as_view(), name="todos"),
    path('AdminTodos/', views.TodosEmpleadosAdmin.as_view(), name="AdminTodos"),
    path('EmpsPorArea/<area>/', views.MyArea.as_view()),
    path('Buscar/', views.VistaBuscar.as_view()),
    path('Habilidades/', views.ListaHabilidades.as_view()),
    path('detail/<pk>/', views.VerDetalle.as_view(), name="detalle"),
    path('crear/', views.CrearEmpleado.as_view(), name="NuevoEmpleado"),
    path('editar/<pk>/', views.EditarEmpleado.as_view(), name='editarEmpleado'),
]
