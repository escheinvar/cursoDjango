from django.urls import path
from . import views

## ursl de la App home
app_name ="deptos_app"

urlpatterns = [
    path('deptos/', views.VerDepto.as_view(), name="verDepto"),
]
