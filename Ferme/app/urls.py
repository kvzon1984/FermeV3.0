

from django.contrib.admin.sites import AdminSite
from django.urls import path
from .views import home,registro,userPass, agregarProducto,eliminar_Producto,listar_producto,modificar_Producto,agregar_OrdenCompra
from .views import listar_OrdenCompra,modificar_OrdenCompra,eliminar_ordenCompra,listar_Cliente, agregar_cliente,userPass2,modificar_Cliente
from .views import eliminar_Cliente,listar_user,eliminar_User


urlpatterns = [
    path('', home, name="home"),
    path('admin/', AdminSite , name='admin'),
    path('registro/', registro, name="registro"),
    path('userPass/', userPass, name="userPass" ),
    path('agregarProducto/', agregarProducto, name="agregarProducto"),
    path('listarProducto/', listar_producto,name='listarProducto'),
    path('modificar_Producto/<id>/', modificar_Producto,name= 'modificarProducto'),   
    path('eliminar_Producto/<id>/', eliminar_Producto, name='eliminarProducto'),
    path('agregar_OrdenCompra/',agregar_OrdenCompra,name='agregarOrdenCompra'),
    path('listar_OrdenCompra/',listar_OrdenCompra, name='listarOrdenCompra'),
    path('modificar_OrdenCompra/<id>/', modificar_OrdenCompra, name= 'modificarOrdenCompra'),
    path('eliminar_OrdenCompra/<id>/', eliminar_ordenCompra,name='eliminarOrdenCompra'),
    path('agregar_Cliente/', agregar_cliente, name='agregarCliente'),
    path('userPass2/', userPass2,name='userPass2'),
    path('listar_Cliente/', listar_Cliente, name='listarCliente'),
    path('modificar_cliente/<id>/', modificar_Cliente, name='modificarCliente'),
    path('eliminar_Cliente/<id>/', eliminar_Cliente, name= 'eliminarCliente'),
    path('listarUser/',listar_user, name='listarUser'),
    path('eliminar_User/<id>/', eliminar_User ,name='eliminarUser')
    
]
