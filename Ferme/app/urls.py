

from django import forms
from django.contrib.admin.sites import AdminSite
from django.urls import path
from django.urls.conf import include
from .views import home,registro,userPass, agregarProducto,eliminar_Producto,listar_producto,modificar_Producto,agregar_Orden_Compra
from .views import listar_OrdenCompra,modificar_OrdenCompra,eliminar_ordenCompra,listar_Cliente, agregar_cliente,userPass2,modificar_Cliente
from .views import eliminar_Cliente,listar_user,eliminar_User,listar_TrazabilidadOC,agregar_Proveedor,listar_Proveedor,eliminar_Proveedor
from .views import modificar_Proveedor,agregarTipoProducto,agregarFamiliaProducto,carroPrueba
 

urlpatterns = [
    path('', home, name="home"),
    path('admin/', AdminSite , name='admin'),
    path('registro/', registro, name="registro"),
    path('userPass/', userPass, name="userPass" ),
    path('agregarProducto/', agregarProducto, name="agregarProducto"),
    path('listarProducto/', listar_producto,name='listarProducto'),
    path('modificar_Producto/<id>/', modificar_Producto,name= 'modificarProducto'),   
    path('eliminar_Producto/<id>/', eliminar_Producto, name='eliminarProducto'),
    path('agregar_OrdenCompra/',agregar_Orden_Compra,name='agregarOrdenCompra'),
    path('listar_OrdenCompra/',listar_OrdenCompra, name='listarOrdenCompra'),
    path('modificar_OrdenCompra/<id>/', modificar_OrdenCompra, name= 'modificarOrdenCompra'),
    path('eliminar_OrdenCompra/<id>/', eliminar_ordenCompra,name='eliminarOrdenCompra'),
    path('agregar_Cliente/', agregar_cliente, name='agregarCliente'),
    path('userPass2/', userPass2,name='userPass2'),
    path('listar_Cliente/', listar_Cliente, name='listarCliente'),
    path('modificar_cliente/<id>/', modificar_Cliente, name='modificarCliente'),
    path('eliminar_Cliente/<id>/', eliminar_Cliente, name= 'eliminarCliente'),
    path('listarUser/',listar_user, name='listarUser'),
    path('eliminar_User/<id>/', eliminar_User ,name='eliminarUser'),
    path('listarTrazabilidadOC/', listar_TrazabilidadOC, name='listar_TOC'),
    path('agregar_proveedor/',agregar_Proveedor, name='agregarProveedor'),
    path('listar_Proveedores/', listar_Proveedor, name='listarProveedor'),
    path('modificar_Proveedor/<id>/', modificar_Proveedor, name= 'modificarProveedor'),
    path('eliminar_Proveedor/<id>/', eliminar_Proveedor ,name='eliminarProveedor'),
    path('agregarTipoTpoducto/', agregarTipoProducto, name='agregarTipoProducto'),
    path('agregarFamiliaTpoducto/', agregarFamiliaProducto, name='agregarFamiliaProducto'),
    path('carroPrueba/', carroPrueba, name='carroPrueba'),
    
    

  
  

    
    
]
