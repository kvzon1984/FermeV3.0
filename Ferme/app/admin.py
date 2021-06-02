from django.contrib import admin
from django.contrib.admin.options import ModelAdmin
from .models import Cliente,Cargo,Comuna, Despacho,DetalleOrdenCompra,DetalleVenta,Empleado,EstadoDespacho,EstadoOrdenCompra,FamiliaProducto,OrdenesCompra,Producto,Proveedor,TipoCliente,TipoDocumento,TipoProducto,TrazabilidadOc,Venta,ZonaDespacho

class CargoAdmin(admin.ModelAdmin):
    list_display = ['id_cargo', 'descripcion']

class ClienteAdmin(admin.ModelAdmin):
    list_display = ['run_cliente', 'dvrun', 'pnombre', 'appaterno', 'id_comuna']
    list_filter = ['id_comuna']
    search_fields = ['pnombre', 'run_cliente']
    list_per_page = 10

class ComunaAdmin(admin.ModelAdmin):
    list_display = ['id_comuna', 'descripcion']
    list_per_page = 10
    search_fields = ['descripcion']

class DespachoAdmin(admin.ModelAdmin):
    list_display = ['id_despacho', 'recibido_por', 'direccion_despacho', 'num_documento']

class DetalleOrdenCompraAdmin(admin.ModelAdmin):
    list_display = ['id_detalle_oc', 'numorden', 'cod_producto', 'cantidad']

class EmpleadoAdmin (admin.ModelAdmin):
    list_display = ['run_emp', 'dvrun_emp', 'pnombre_emp', 'snombre_emp', 'appaterno_emp', 'apmaterno_emp', 'id_cargo' ]
    list_filter= ['id_cargo']
    search_fields = ['run_emp']
    list_per_page = 10

class ProductoAdmin(admin.ModelAdmin):
    list_display=['cod_producto','descripcion','fecha_vencimiento','stock','stock_critico','precio','cod_proveedor','cod_familia','cod_tipo_producto']
    list_filter=['cod_producto', 'precio']
    search_fields = ['descripcion']
    list_per_page = 10

class TipoProductoAdmin(admin.ModelAdmin):
    list_display=['cod_tipo_producto','descripcion']

class FamiliaProductoAdmin(admin.ModelAdmin):
    list_display=['cod_familia', 'descripcion']

class OrdenCompraAdmin(admin.ModelAdmin):
    list_display=['numorden','cod_proveedor','run_empleado','estado', 'fecha_emision','fecha_recepcion']


class ProveedorAdmin(admin.ModelAdmin):
    
    list_display=['cod_proveedor','run_proveedor','nom_proveedor','celular_proveedor']

class EstadoOrdenCompraAdmin(admin.ModelAdmin):
    list_display=['id_estado_orden','descripcion']

admin.site.register(Cargo, CargoAdmin)
admin.site.register(Cliente, ClienteAdmin)
admin.site.register(Comuna, ComunaAdmin)
admin.site.register(Despacho, DespachoAdmin)
admin.site.register(DetalleOrdenCompra, DetalleOrdenCompraAdmin)
admin.site.register(DetalleVenta)
admin.site.register(Empleado, EmpleadoAdmin)
admin.site.register(EstadoDespacho)
admin.site.register(EstadoOrdenCompra, EstadoOrdenCompraAdmin)
admin.site.register(FamiliaProducto,FamiliaProductoAdmin)
admin.site.register(OrdenesCompra,OrdenCompraAdmin)
admin.site.register(Producto, ProductoAdmin)
admin.site.register(Proveedor,ProveedorAdmin)
admin.site.register(TipoCliente)
admin.site.register(TipoDocumento)
admin.site.register(TipoProducto,TipoProductoAdmin)
admin.site.register(TrazabilidadOc)
admin.site.register(Venta)
admin.site.register(ZonaDespacho)
