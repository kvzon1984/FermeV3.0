
from .carro import Carro
from django.shortcuts import redirect,render
from app.models import Producto

# Create your views here.
#funciones para carrito

def agregar_productos_carrito(request,id):
    carro = Carro(request)
    producto = Producto.objects.get(cod_producto= id)
    carro.agregar(producto = producto)
    return redirect("home")

def eliminar_producto_carrito(request, id):
    carro = Carro(request)
    producto = Producto.objects.get(cod_producto = id)
    carro.eliminar(producto = producto)
    return redirect("home")

def restar_producto_carrito(request,id):
    carro = Carro(request)
    producto = Producto.objects.get(cod_producto = id)
    carro.restar_productos(producto = producto)
    return redirect("home")

def limpiar_carrito(request):
    carro = Carro(request)
    carro.limpiar_carro()
    return redirect("home")


        