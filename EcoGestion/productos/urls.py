from django.urls import path
from . import views

app_name = 'productos'

urlpatterns = [
    path('', views.producto_list, name='producto_list'),
    path('nuevo/', views.producto_create, name='producto_create'),
    path('editar/<int:pk>/', views.producto_update, name='producto_update'),
    path('eliminar/<int:pk>/', views.producto_delete, name='producto_delete'),
    path('existencias/<int:pk>/', views.producto_stock_update, name='producto_stock_update'),

    path('asignaciones/', views.asignacion_list, name='asignacion_list'),
    path('asignar/', views.asignar_producto, name='asignar_producto'),
    path('asignaciones/eliminar/<int:pk>/', views.asignacion_delete, name='asignacion_delete'),
]

