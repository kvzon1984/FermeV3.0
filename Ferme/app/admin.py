from django.contrib import admin
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


admin.site.register(Cargo, CargoAdmin)
admin.site.register(Cliente, ClienteAdmin)
admin.site.register(Comuna, ComunaAdmin)
admin.site.register(Despacho, DespachoAdmin)
admin.site.register(DetalleOrdenCompra, DetalleOrdenCompraAdmin)
admin.site.register(DetalleVenta)
admin.site.register(Empleado)
admin.site.register(EstadoDespacho)
admin.site.register(EstadoOrdenCompra)
admin.site.register(FamiliaProducto)
admin.site.register(OrdenesCompra)
admin.site.register(Producto)
admin.site.register(Proveedor)
admin.site.register(TipoCliente)
admin.site.register(TipoDocumento)
admin.site.register(TipoProducto)
admin.site.register(TrazabilidadOc)
admin.site.register(Venta)
admin.site.register(ZonaDespacho)
