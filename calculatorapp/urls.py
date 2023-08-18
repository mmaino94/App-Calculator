from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.calculadora, name='calculadora'),
    path('tabla-formulario2/', views.tabla_formulario2, name='tabla_formulario2'),
    path('agregar-instrumento-factor/', views.agregar_instrumento_factor, name='agregar_instrumento_factor'),
    path('editar-instrumento-factor/<int:pk>/', views.editar_instrumento_factor, name='editar_instrumento_factor'),
    path('tabla-formulario1/', views.tabla_formulario1, name='tabla_formulario1'),
    
    ]