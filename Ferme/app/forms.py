from django import forms
from .models import Cliente
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
