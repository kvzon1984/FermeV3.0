from django import forms
from django.forms import fields
from .models import Cliente, Producto,OrdenesCompra
from django.contrib.auth.forms import UserCreationForm

class RegistroForm(forms.ModelForm):

    class Meta:
        model = Cliente
       
        fields = [
            "pnombre", 
            "snombre" , 
            "appaterno",
            "apmaterno", 
            "run_cliente", 
            "dvrun", 
            "fecha_nacimiento", 
            "celular",
            "correo",
            "direccion",
            "id_comuna",
            "cod_tipo_cliente",
            "razon_social",
            ]

class UserPass(UserCreationForm):
    pass
        

class AgregarProductoForm(forms.ModelForm):
    class Meta:
        model = Producto
        fields = [
            'descripcion',
            'fecha_vencimiento',
            'stock',
            'stock_critico',
            'precio',
            'foto',
            'cod_proveedor',
            'cod_familia',
            'cod_tipo_producto'
        ]

class AgregarOrdenCompra(forms.ModelForm):
    class Meta:
        model = OrdenesCompra
        fields = '__all__'


