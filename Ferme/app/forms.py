
from django import forms
from django.db.models import fields
from django.forms import widgets
from .models import Cliente, Empleado, FamiliaProducto, Producto,OrdenesCompra,Proveedor, TipoCliente, TipoProducto,Comuna
from django.contrib.auth.forms import UserCreationForm

class DateInput(forms.DateInput):
    input_type = 'date'
    
    

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
            "razon_social"
            ]

        labels = {
            "pnombre" : 'Primer nombre', 
            "snombre"  : '<br>Segundo nombre' ,
            "appaterno" : '<br>Apellido paterno',
            "apmaterno" : '<br>Apellido materno',
            "run_cliente" : '<br>Rut Cliente', 
            "dvrun" : '<br>dv' ,
            "fecha_nacimiento": '<br>Fecha de nacimiento', 
            "celular": '<br>Telefono',
            "correo": '<br>Email',
            "direccion" : '<br>Direccion',
            "id_comuna" : '<br>Comuna',
            "cod_tipo_cliente" : '<br>Tipo de Cliente',
            "razon_social" : ''
        }
        widgets = {
            'run_cliente' : forms.TextInput(attrs={'class':'input','placeholder':'12345678'}),
            'fecha_nacimiento': DateInput(),
            'razon_social':forms.TextInput(attrs={'hidden':'hidden'})
        }

    id_comuna = forms.ModelChoiceField(
        queryset= Comuna.objects.all(),
        label='<br>Comuna'
    )

    cod_tipo_cliente = forms.ModelChoiceField(
        queryset= TipoCliente.objects.all(),
        label='<br>Tipo de Cliente'
    )


        

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


            
        labels = {
            "descripcion":'Nombre del producto',
            "fecha_vencimiento":'<br>Fecha de vencimiento',
            "stock":'<br>Stock',
            "stock_critico":' <br>Stock critico',
            "precio":' <br>Precio',
            "foto":' <br>Seleccione la imagen del producto'
          
        }
        
    
        widgets = {
            "descripcion": forms.TextInput(attrs={'class':'input','placeholder':'Ingrese el nombre del producto'}),
            "fecha_vencimiento":DateInput(attrs={'type':'date'})
        }    
    cod_tipo_producto = forms.ModelChoiceField(
        queryset = TipoProducto.objects.all(),
        label='<br>Tipo Productos'
    
    )

    cod_proveedor = forms.ModelChoiceField(
        queryset = Proveedor.objects.all(),
        label='<br>Proveedor'
    
    )
    

    cod_familia = forms.ModelChoiceField(
        queryset = FamiliaProducto.objects.all(),
        label='<br>Familia de producto'
    
    )


#agregar empleado
#class EmpleadoAgregarOrdenCompra(forms.ModelForm):
#    class Meta:
 #       model = Empleado

  #  fields = {
   #     'id_cargo'
    #}

class AgregarOrdenCompra(forms.ModelForm):
    class Meta:
        model = OrdenesCompra
       
        fields = [
            
            'cod_proveedor',
            'run_empleado',
            'estado',
            'fecha_emision',
            'fecha_recepcion'
            
        ]
        labels={
            "cod_proveedor":'Codigo Proveedor ',
            "run_empleado":'<br>Rut Empleado',
            "estado":'<br>Estado Orden Compra',
            "fecha_emision":'<br>Fecha Emision',
            "fecha_recepcion":'<br>Fecha Recepcion',
            
        }
        widgets = {
            'fecha_emision': DateInput(),
            'fecha_recepcion': DateInput()
        }
    
 



class ProveedorForm(forms.ModelForm):

    class Meta:
        model= Proveedor
        fields = [
            'run_proveedor','nom_proveedor','celular_proveedor'
        ]
        labels={
            "run_proveedor":'Rut Proveedor ',
            "nom_proveedor":'<br>Nombre',
            "celular_proveedor":'<br>Celular ',
        }
        widgets = {
        
            "run_proveedor": forms.TextInput(attrs={'class':'input','placeholder':'12345678-1'}),
            "nom_proveedor": forms.TextInput(attrs={'class':'input','placeholder':'Ingrese Datos'}),
            "celular_proveedor": forms.TextInput(attrs={'class':'input','placeholder':'91234567'}),
            
        }

class TipoProductoForm(forms.ModelForm):
    class Meta:
        model = TipoProducto
        fields = [
            
            'descripcion'
        ]

      
        labels={
            'descripcion': 'Nombre de Tipo Producto'
        }

        widgets = {
            "descripcion": forms.TextInput(attrs={'class':'input','placeholder':'Ingrese un tipo de producto','title':'Tipo de producto' }),
        }

class FamiliaProductoForm(forms.ModelForm):
    class Meta:
        model = FamiliaProducto
        fields = [
            'descripcion'
        ]


        labels = {
            'descripcion': 'Familia del producto'
        }

        widgets = {'descripcion': forms.TextInput(attrs={'class' : 'input'})}
