from django import forms
from django.forms import fields
from .models import Cliente, Producto,Empleado
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
        fields = '__all__'

class AgregarEmpleadoForm(forms.ModelForm):
    class Meta:
        model = Empleado
        fields = '__all__'