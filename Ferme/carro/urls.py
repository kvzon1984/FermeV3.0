from django.urls import path
from .import views

app_name= "carro"
urlpatterns =[

    path("agregar/<int:id>L/", views.agregar_productos_carrito, name='agregar_producto_carro'),
    path("eliminar/<int:id>L/", views.eliminar_producto_carrito, name='eliminar_producto_carro'),
    path("restar/<int:id>L/", views.restar_producto_carrito, name='restar_producto_carro'),
    path("limpiar/", views.limpiar_carrito, name='limpiar_carrito'),
]