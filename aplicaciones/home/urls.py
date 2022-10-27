from django.urls import path
from . import views
## ursl de la App home
urlpatterns = [
    path('prueba/', views.MyClase.as_view()),
    path('prueba3/', views.MyClase2.as_view()),
    path('prueba2/', views.MyClase3.as_view()),
    path('form/', views.PruebaCreateView.as_view(), name='prueba_add'),
]
