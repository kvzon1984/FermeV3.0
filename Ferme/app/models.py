# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class AdminInterfaceTheme(models.Model):
    name = models.CharField(unique=True, max_length=50, blank=True, null=True)
    active = models.BooleanField()
    title = models.CharField(max_length=50, blank=True, null=True)
    title_visible = models.BooleanField()
    logo = models.CharField(max_length=100, blank=True, null=True)
    logo_visible = models.BooleanField()
    css_header_background_color = models.CharField(max_length=10, blank=True, null=True)
    title_color = models.CharField(max_length=10, blank=True, null=True)
    css_header_text_color = models.CharField(max_length=10, blank=True, null=True)
    css_header_link_color = models.CharField(max_length=10, blank=True, null=True)
    css_header_link_hover_color = models.CharField(max_length=10, blank=True, null=True)
    css_module_background_color = models.CharField(max_length=10, blank=True, null=True)
    css_module_text_color = models.CharField(max_length=10, blank=True, null=True)
    css_module_link_color = models.CharField(max_length=10, blank=True, null=True)
    css_module_link_hover_color = models.CharField(max_length=10, blank=True, null=True)
    css_module_rounded_corners = models.BooleanField()
    css_generic_link_color = models.CharField(max_length=10, blank=True, null=True)
    css_generic_link_hover_color = models.CharField(max_length=10, blank=True, null=True)
    css_save_button_background5185 = models.CharField(max_length=10, blank=True, null=True)
    css_save_button_backgroundd677 = models.CharField(max_length=10, blank=True, null=True)
    css_save_button_text_color = models.CharField(max_length=10, blank=True, null=True)
    css_delete_button_backgroucea0 = models.CharField(max_length=10, blank=True, null=True)
    css_delete_button_backgrou6352 = models.CharField(max_length=10, blank=True, null=True)
    css_delete_button_text_color = models.CharField(max_length=10, blank=True, null=True)
    css = models.TextField(blank=True, null=True)
    list_filter_dropdown = models.BooleanField()
    related_modal_active = models.BooleanField()
    related_modal_background_color = models.CharField(max_length=10, blank=True, null=True)
    related_modal_rounded_corners = models.BooleanField()
    logo_color = models.CharField(max_length=10, blank=True, null=True)
    recent_actions_visible = models.BooleanField()
    favicon = models.CharField(max_length=100, blank=True, null=True)
    related_modal_background_o7c6e = models.CharField(max_length=5, blank=True, null=True)
    env_name = models.CharField(max_length=50, blank=True, null=True)
    env_visible_in_header = models.BooleanField(blank=True, null=True)
    env_color = models.CharField(max_length=10, blank=True, null=True)
    env_visible_in_favicon = models.BooleanField()
    related_modal_close_button8203 = models.BooleanField()
    language_chooser_active = models.BooleanField()
    language_chooser_display = models.CharField(max_length=10, blank=True, null=True)
    list_filter_sticky = models.BooleanField()

    class Meta:
        managed = False
        db_table = 'admin_interface_theme'


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=150, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255, blank=True, null=True)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128, blank=True, null=True)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.BooleanField()
    username = models.CharField(unique=True, max_length=150, blank=True, null=True)
    first_name = models.CharField(max_length=150, blank=True, null=True)
    last_name = models.CharField(max_length=150, blank=True, null=True)
    email = models.CharField(max_length=254, blank=True, null=True)
    is_staff = models.BooleanField()
    is_active = models.BooleanField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class Cargo(models.Model):
    id_cargo = models.IntegerField(primary_key=True)
    descripcion = models.CharField(max_length=30)

    class Meta:
        managed = False
        db_table = 'cargo'


class Cliente(models.Model):
    run_cliente = models.IntegerField(primary_key=True)
    dvrun = models.CharField(max_length=1)
    pnombre = models.CharField(max_length=50)
    snombre = models.CharField(max_length=50, blank=True, null=True)
    appaterno = models.CharField(max_length=50)
    apmaterno = models.CharField(max_length=50, blank=True, null=True)
    fecha_nacimiento = models.DateField()
    celular = models.CharField(max_length=12)
    correo = models.CharField(max_length=255, blank=True, null=True)
    direccion = models.CharField(max_length=255)
    razon_social = models.CharField(max_length=50, blank=True, null=True)
    cod_tipo_cliente = models.ForeignKey('TipoCliente', models.DO_NOTHING, db_column='cod_tipo_cliente')
    id_comuna = models.ForeignKey('Comuna', models.DO_NOTHING, db_column='id_comuna')

    class Meta:
        managed = False
        db_table = 'cliente'


class Comuna(models.Model):
    id_comuna = models.IntegerField(primary_key=True)
    descripcion = models.CharField(max_length=30)

    class Meta:
        managed = False
        db_table = 'comuna'


class Despacho(models.Model):
    id_despacho = models.IntegerField(primary_key=True)
    fecha_despacho = models.DateField(blank=True, null=True)
    recibido_por = models.CharField(max_length=255)
    direccion_despacho = models.CharField(max_length=255)
    celular = models.CharField(max_length=12)
    foto = models.BinaryField(blank=True, null=True)
    num_documento = models.ForeignKey('Venta', models.DO_NOTHING, db_column='num_documento')
    id_zona = models.ForeignKey('ZonaDespacho', models.DO_NOTHING, db_column='id_zona')
    id_estado_des = models.ForeignKey('EstadoDespacho', models.DO_NOTHING, db_column='id_estado_des')
    id_comuna = models.ForeignKey(Comuna, models.DO_NOTHING, db_column='id_comuna')

    class Meta:
        managed = False
        db_table = 'despacho'


class DetalleOrdenCompra(models.Model):
    id_detalle_oc = models.IntegerField(primary_key=True)
    numorden = models.ForeignKey('OrdenesCompra', models.DO_NOTHING, db_column='numorden')
    cod_producto = models.ForeignKey('Producto', models.DO_NOTHING, db_column='cod_producto')
    cantidad = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'detalle_orden_compra'


class DetalleVenta(models.Model):
    id_detalle_venta = models.IntegerField(primary_key=True)
    valor_unitario = models.IntegerField()
    cantidad = models.IntegerField()
    tot_linea = models.IntegerField()
    num_documento = models.ForeignKey('Venta', models.DO_NOTHING, db_column='num_documento')
    cod_producto = models.ForeignKey('Producto', models.DO_NOTHING, db_column='cod_producto')

    class Meta:
        managed = False
        db_table = 'detalle_venta'


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200, blank=True, null=True)
    action_flag = models.IntegerField()
    change_message = models.TextField(blank=True, null=True)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100, blank=True, null=True)
    model = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    app = models.CharField(max_length=255, blank=True, null=True)
    name = models.CharField(max_length=255, blank=True, null=True)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField(blank=True, null=True)
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'


class Empleado(models.Model):
    run_emp = models.IntegerField(primary_key=True)
    dvrun_emp = models.CharField(max_length=1)
    pnombre_emp = models.CharField(max_length=50)
    snombre_emp = models.CharField(max_length=50, blank=True, null=True)
    appaterno_emp = models.CharField(max_length=50)
    apmaterno_emp = models.CharField(max_length=50, blank=True, null=True)
    id_cargo = models.ForeignKey(Cargo, models.DO_NOTHING, db_column='id_cargo')

    class Meta:
        managed = False
        db_table = 'empleado'


class EstadoDespacho(models.Model):
    id_estado_des = models.IntegerField(primary_key=True)
    descripcion = models.CharField(max_length=13)

    class Meta:
        managed = False
        db_table = 'estado_despacho'


class EstadoOrdenCompra(models.Model):
    id_estado_orden = models.IntegerField(primary_key=True)
    descripcion = models.CharField(max_length=7)

    class Meta:
        managed = False
        db_table = 'estado_orden_compra'


class FamiliaProducto(models.Model):
    cod_familia = models.IntegerField(primary_key=True)
    descripcion = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'familia_producto'


class OrdenesCompra(models.Model):
    numorden = models.IntegerField(primary_key=True)
    cod_proveedor = models.ForeignKey('Proveedor', models.DO_NOTHING, db_column='cod_proveedor')
    run_empleado = models.ForeignKey(Empleado, models.DO_NOTHING, db_column='run_empleado')
    estado = models.CharField(max_length=10)
    fecha_emision = models.DateField()
    fecha_recepcion = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ordenes_compra'


class Producto(models.Model):
    cod_producto = models.BigIntegerField(primary_key=True)
    descripcion = models.CharField(max_length=255)
    fecha_vencimiento = models.DateField(blank=True, null=True)
    stock = models.IntegerField()
    stock_critico = models.IntegerField()
    precio = models.IntegerField(blank=True, null=True)
    foto = models.BinaryField(blank=True, null=True)
    cod_proveedor = models.IntegerField()
    cod_familia = models.ForeignKey(FamiliaProducto, models.DO_NOTHING, db_column='cod_familia')
    cod_tipo_producto = models.ForeignKey('TipoProducto', models.DO_NOTHING, db_column='cod_tipo_producto')

    class Meta:
        managed = False
        db_table = 'producto'


class Proveedor(models.Model):
    cod_proveedor = models.IntegerField(primary_key=True)
    run_proveedor = models.CharField(max_length=10)
    nom_proveedor = models.CharField(max_length=255)
    celular_proveedor = models.CharField(max_length=12)

    class Meta:
        managed = False
        db_table = 'proveedor'


class TipoCliente(models.Model):
    cod_tipo_cliente = models.IntegerField(primary_key=True)
    nombre_tipo_cliente = models.CharField(max_length=7)

    class Meta:
        managed = False
        db_table = 'tipo_cliente'


class TipoDocumento(models.Model):
    id_documento = models.IntegerField(primary_key=True)
    descripcion = models.CharField(max_length=7)

    class Meta:
        managed = False
        db_table = 'tipo_documento'


class TipoProducto(models.Model):
    cod_tipo_producto = models.IntegerField(primary_key=True)
    descripcion = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'tipo_producto'


class TrazabilidadOc(models.Model):
    id_trazabilidad_oc = models.IntegerField(primary_key=True)
    numorden = models.ForeignKey(OrdenesCompra, models.DO_NOTHING, db_column='numorden')
    fecha = models.DateField()
    id_estado_orden = models.ForeignKey(EstadoOrdenCompra, models.DO_NOTHING, db_column='id_estado_orden', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'trazabilidad_oc'


class Venta(models.Model):
    num_documento = models.IntegerField(primary_key=True)
    run_cliente = models.ForeignKey(Cliente, models.DO_NOTHING, db_column='run_cliente', blank=True, null=True)
    fecha = models.DateField()
    neto = models.IntegerField(blank=True, null=True)
    iva = models.IntegerField(blank=True, null=True)
    total = models.IntegerField()
    estado = models.CharField(max_length=7)
    run_empleado = models.IntegerField()
    id_documento = models.ForeignKey(TipoDocumento, models.DO_NOTHING, db_column='id_documento')
    id_anulacion = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'venta'


class ZonaDespacho(models.Model):
    id_zona = models.IntegerField(primary_key=True)
    nom_sector = models.CharField(max_length=50)
    monto_despacho = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'zona_despacho'
