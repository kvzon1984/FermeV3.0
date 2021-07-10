from os import path
from .models import   AuthUser, OrdenesCompra, Producto, Cliente, Proveedor, TipoProducto,TrazabilidadOc,FamiliaProducto
from django.shortcuts import render,redirect,get_object_or_404
from .forms import AgregarOrdenCompra, FamiliaProductoForm, ProveedorForm, RegistroForm, TipoProductoForm,UserPass,AgregarProductoForm
from django.db import connection
from django.contrib import messages

import cx_Oracle


# Create your views here.


def home(request):

    productos = Producto.objects.all()

    data= {
        'productos':productos
    }


    return render(request, 'app/home.html',data)

def carroPrueba(request):

    

    return render(request, 'app/Carrito/variableCarro.html' )





def registro(request):
    
    data={
        'form': RegistroForm(),
   
    } 
    
    if request.method == 'POST':
        
        formulario = RegistroForm(data = request.POST)
        print(data)
        if formulario.is_valid():
            formulario.save()
            return redirect(to="userPass")
        else:
            data['form'] = formulario
    return render(request, 'registration/registro.html', data)


def userPass(request):
    data= {
        'form' : UserPass()
    }

    if request.method == 'POST':
        formulario = UserPass(data=request.POST)
        if formulario.is_valid():
            formulario.save()
            messages.success (request, "Usuario creado Correctamente, Puede ingresar y disfrutar de nuestros servicios")
            return redirect(to="login")

        data['form'] = formulario
        
           
    return render(request, 'registration/userPass.html', data)




def agregarProducto(request):

    data={
        'form' : AgregarProductoForm()
    }

    if request.method == 'POST':
        descripcion = request.POST.get('descripcion')
        fecha_vencimiento = request.POST.get('fecha_vencimiento')
        if not fecha_vencimiento:
            fecha_vencimiento = None
        stock = request.POST.get('stock')
        stock_critico = request.POST.get('stock_critico')
        precio = request.POST.get('precio')
        foto = request.POST.get('foto')
        cod_proveedor = request.POST.get('cod_proveedor')
        cod_familia = request.POST.get('cod_familia')
        cod_tipo_producto = request.POST.get('cod_tipo_producto')
        
        #llamo a la funcion
        v_salida = generar_cod_Producto(descripcion,fecha_vencimiento,stock,stock_critico,precio,foto, cod_proveedor,cod_familia,cod_tipo_producto)
        if v_salida == 1 :
            
            messages.success (request, "Producto ingresado Correctamente")

            return redirect(to="listarProducto")
        else :
            messages.error (request, "Algo salio mal... Codigo ya existe")
            
    return render(request,'app/producto/agregar.html',data)

def agregarTipoProducto(request):

    data={
        'form' : TipoProductoForm(),
        'form2':listar_Tipo_producto()
    }

    if request.method == 'POST':
        descripcion = request.POST.get('descripcion')
        
        v_salida = generar_Cod_Tipo_Producto(descripcion)# llamo a la Funciones
        if v_salida == 1 :
            
            messages.success (request, "Producto ingresado Correctamente")

            return redirect(to="agregarTipoProducto")
        else :
            messages.error (request, "Algo salio mal... Codigo ya existe")
            
    return render(request,'app/producto/agregarTipoProducto.html',data)


def agregarFamiliaProducto(request):

    data={
        'form' : FamiliaProductoForm(),
        'form2':listar_familia_producto()
    }


    if request.method == 'POST':
        descripcion = request.POST.get('descripcion')
        
        v_salida = generar_Cod_Familia_Producto(descripcion)# llamo a la Funciones
        if v_salida == 1 :
            
            messages.success (request, "Producto ingresado Correctamente")

            return redirect(to="agregarFamiliaProducto")
        else :
            messages.error (request, "Algo salio mal... Codigo ya existe")
            
    return render(request,'app/producto/agregarFamiliaProducto.html',data)

def listar_familia_producto():

    familiaproductos = FamiliaProducto.objects.all()

    return familiaproductos

def listar_Tipo_producto():

    tipoproductos = TipoProducto.objects.all()

    return tipoproductos

def listar_producto(request):

    productos = Producto.objects.all()
    
    data={
        'form': productos
    }
    return render(request,'app/producto/listar.html',data) 
    

def modificar_Producto(request, id):

    cod_producto =int(id)
    producto = get_object_or_404(Producto, cod_producto=cod_producto)
    data= {
        'form' :  AgregarProductoForm(instance=producto)
    }

    if request.method == 'POST':
        formulario = AgregarProductoForm(data=request.POST,instance=producto, files=request.FILES)
        if formulario.is_valid():
            formulario.save()
            data['form'] = formulario
            messages.success (request, "Producto Modificado Correctamente")
            return redirect(to="listarProducto")
        data['form'] = formulario

    return render(request,'app/producto/modificar.html', data)


def eliminar_Producto(request, id):

    cod_producto = int(id)
    producto = get_object_or_404(Producto, cod_producto = cod_producto)
    producto.delete()
    messages.success (request, "Producto Eliminado! ")
    return redirect(to="listarProducto") 


def agregar_Orden_Compra(request):

    data={
        'form': AgregarOrdenCompra(),
   
    } 
    
    if request.method == 'POST':
        cod_proveedor = request.POST.get('cod_proveedor')
        run_empleado = request.POST.get('run_empleado')
        estado = request.POST.get('estado')
        fecha_emision = request.POST.get('fecha_emision')
        fecha_recepcion = request.POST.get('fecha_recepcion')
          
        v_salida = generar_cod_OrdenCompra(cod_proveedor,run_empleado,estado,fecha_emision,fecha_recepcion,)
        if v_salida == 1 :
            
            messages.success (request, "Orden Compra Ingresado Correctamente")
    
            return redirect(to="listarOrdenCompra")
        else :
            messages.error (request,"mensaje"+str(v_salida)+" cod "+str(cod_proveedor)+" rn "+str(run_empleado)+" es "+str(estado)+" fe "+str(fecha_emision)+" fr "+str(fecha_recepcion))
    return render(request,'app/ordenCompra/agregar.html',data)



def listar_OrdenCompra(request):

    productos = OrdenesCompra.objects.all()
    
    data={
        'form': productos
    }
    return render(request,'app/ordenCompra/listar.html',data) 


def modificar_OrdenCompra(request, id):
    
    OrdenCompra = get_object_or_404(OrdenesCompra, numorden = id)
   
    data= {
        'form' :  AgregarOrdenCompra(instance=OrdenCompra)
    }

    if request.method == 'POST':
        formulario = AgregarOrdenCompra(data=request.POST,instance=OrdenCompra, files=request.FILES)
        if formulario.is_valid():
            formulario.save()
            messages.success (request, "Orden de Compra modificada con exito!")
            return redirect(to="listarOrdenCompra")
        data['form'] = formulario

    return render(request,'app/ordenCompra/modificar.html',data)


def eliminar_ordenCompra(request, id):

    OrdenCompra = get_object_or_404(OrdenesCompra, numorden = id)
    OrdenCompra.delete()
    messages.success (request, "Orden de compra Eliminada")
    return redirect(to="listarOrdenCompra")


def agregar_cliente(request):

    data={
        'form': RegistroForm(),
   
    } 
    
    if request.method == 'POST':
        
        formulario = RegistroForm(data = request.POST)
   
        if formulario.is_valid():
            formulario.save()
            return redirect(to="userPass2")
        else:
            data['form'] = formulario

    return render(request,'app/cliente/agregar.html',data)


def userPass2(request):
    data= {
        'form' : UserPass()
    }

    if request.method == 'POST':
        formulario = UserPass(data=request.POST)
        if formulario.is_valid():
            formulario.save()
            messages.success (request, "Cliente ingresado Correctamente")
            return redirect(to="listarCliente")
        data['form'] = formulario
        
           
    return render(request, 'registration/userPass.html', data)


def listar_Cliente(request):

    clientes = Cliente.objects.all()    
    data={
        'clientes': clientes
    }

    return render(request,'app/cliente/listar.html', data) 


def modificar_Cliente(request, id):
    
    cliente = get_object_or_404(Cliente, run_cliente = id)
    data= {
        'form' :  RegistroForm(instance=cliente)
    }

    if request.method == 'POST':
        formulario = RegistroForm(data=request.POST,instance=cliente, files=request.FILES)
        if formulario.is_valid():
            formulario.save()
            messages.success (request, "Cliente Modoficado Correctamente")
            return redirect(to="listarCliente")
        data['form'] = formulario

    return render(request,'app/cliente/modificar.html',data)


def eliminar_Cliente(request, id):

    cliente = get_object_or_404(Cliente, run_cliente = id)
    cliente.delete()
    messages.success (request, "Cliente Eliminado ")
    return redirect(to="listarCliente")


def listar_user(request):
    usuarios =AuthUser.objects.all()
    
    data={
        'usuarios':usuarios
    }

    return render(request,'app/cliente/listarUser.html', data)


def eliminar_User(request, id):

    user = get_object_or_404(AuthUser, username = id)
    user.delete()
    messages.success (request, "Usuario eliminado")
    return redirect(to="listarUser")


def listar_TrazabilidadOC(request):

    result = TrazabilidadOc.objects.all

    
    return render(request,'app/ordenCompra/listaTrazabilidadOC.html',{'listar_TrazabilidadOC':result}) 


def agregar_Proveedor(request):

    data={
        'form' : ProveedorForm()
    }

    if request.method == 'POST':
        run_proveedor = request.POST.get('run_proveedor')
        nom_proveedor = request.POST.get('nom_proveedor')
        celular_proveedor = request.POST.get('celular_proveedor')
       
        v_salida1 = generar_cod_Proveedor(run_proveedor,nom_proveedor,celular_proveedor)
        if v_salida1 == 1 :
            
            messages.success (request, "Proveedor ingresado Correctamente")

            return redirect(to="listarProveedor")
        else :
            messages.error (request, "Algo salio mal... Codigo ya existe")

    return render(request,'app/proveedor/agregar.html',data)




def listar_Proveedor(request):

    proveedores = Proveedor.objects.all()    
    data={
        'proveedores': proveedores
    }

    return render(request,'app/proveedor/listar.html', data)

def modificar_Proveedor(request, id):
    
    cliente = get_object_or_404(Proveedor, cod_proveedor = id)
    data= {
        'form' :  ProveedorForm(instance=cliente)
    }

    if request.method == 'POST':
        formulario = ProveedorForm(data=request.POST,instance=cliente, files=request.FILES)
        if formulario.is_valid():
            formulario.save()
            messages.success (request, "Proveedor modificado correctamente")
            return redirect(to="listarProveedor")
        data['form'] = formulario

    return render(request,'app/proveedor/modificar.html',data)

def eliminar_Proveedor(request, id):

    user = get_object_or_404(Proveedor, cod_proveedor = id)
    user.delete()
    messages.success (request, "Proveedor eliminado")
    return redirect(to="listarProveedor")



#def que corresponde a los Procedimientos almacenados

def generar_Cod_Tipo_Producto(descripcion):

    django_cursor= connection.cursor()
    cursor= django_cursor.connection.cursor()
    v_salida= cursor.var(cx_Oracle.NUMBER)
    #llamo al procedimiento almacenado desde oracle
    cursor.callproc("PA_INSERTAR_TIPO_PRO", [descripcion,v_salida])
    return v_salida.getvalue()

def generar_Cod_Familia_Producto(descripcion):

    django_cursor= connection.cursor()
    cursor= django_cursor.connection.cursor()
    v_salida= cursor.var(cx_Oracle.NUMBER)
    #llamo al procedimiento almacenado desde oracle
    cursor.callproc("PA_INSERTAR_FAMILIA_PRO", [descripcion,v_salida])
    return v_salida.getvalue()

def generar_cod_Producto(descripcion, fecha_vencimiento,stock,stock_critico,precio,foto,cod_proveedor,cod_familia,cod_tipo_producto):

    django_cursor= connection.cursor()
    cursor= django_cursor.connection.cursor()
    v_salida= cursor.var(cx_Oracle.NUMBER)
     #llamo al procedimiento almacenado desde oracle
    cursor.callproc("PA_GUARDAR_PRODU", [descripcion, fecha_vencimiento,stock,stock_critico,precio,foto,cod_proveedor,cod_familia,cod_tipo_producto,v_salida])
    return v_salida.getvalue()

def generar_cod_OrdenCompra(cod_proveedor, run_empleado,estado,fecha_emision,fecha_recepcion):

    django_cursor= connection.cursor()
    cursor= django_cursor.connection.cursor()
    v_salida= cursor.var(cx_Oracle.NUMBER)

    cursor.callproc("PA_INSERTAR_OC", [cod_proveedor, run_empleado,estado,fecha_emision,fecha_recepcion,v_salida])
    return v_salida.getvalue()

def generar_cod_Proveedor(run_proveedor, nom_proveedor,celular_proveedor):

    django_cursor= connection.cursor()
    cursor= django_cursor.connection.cursor()
    v_salida1= cursor.var(cx_Oracle.NUMBER)

    cursor.callproc("PA_INSERTAR_PROVEEDOR", [run_proveedor, nom_proveedor,celular_proveedor,v_salida1])
    return v_salida1.getvalue()




    #-----------------------------------------------------------



