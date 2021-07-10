from django.urls import path
from .import views

app_name= "carro"
urlpatterns =[

    path("agregar/<int:id>/", views.agregar_productos_carrito, name='agregar_producto_carro'),
    path("eliminar/<int:id>/", views.eliminar_producto_carrito, name='eliminar_producto_carro'),
    path("restar/<int:id>/", views.restar_producto_carrito, name='restar_producto_carro'),
    path("limpiar/", views.limpiar_carrito, name='limpiar_carrito'),
    path("agregar_productos_carrito_dos/<int:id>", views.agregar_productos_carrito_dos, name='agregar_productos_carrito_dos'),
    

]