
from django.db.models import fields
from .models import  AuthGroupPermissions, AuthUser, OrdenesCompra, Producto, Cliente
from django.shortcuts import render,redirect,get_object_or_404
from .forms import AgregarOrdenCompra, RegistroForm,UserPass,AgregarProductoForm
from django.db import connection
import cx_Oracle


# Create your views here.


def home(request):

    productos = Producto.objects.all()

    data= {
        'productos':productos
    }


    return render(request, 'app/home.html',data)


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
    return render(request, 'app/registro.html', data)


def userPass(request):
    data= {
        'form' : UserPass()
    }

    if request.method == 'POST':
        formulario = UserPass(data=request.POST)
        if formulario.is_valid():
            formulario.save()
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
        stock = request.POST.get('stock')
        stock_critico = request.POST.get('stock_critico')
        precio = request.POST.get('precio')
        
        foto = request.POST.get('foto')
        print(foto)
        cod_proveedor = request.POST.get('cod_proveedor')
        cod_familia = request.POST.get('cod_familia')
        cod_tipo_producto = request.POST.get('cod_tipo_producto')
        v_salida = generar_cod_Producto(descripcion,fecha_vencimiento,stock,stock_critico,precio,foto, cod_proveedor,cod_familia,cod_tipo_producto)
        if v_salida == 1 :
            
            return redirect(to="listarProducto")
    return render(request,'app/producto/agregar.html',data)

def generar_cod_Producto(descripcion, fecha_vencimiento,stock,stock_critico,precio,foto,cod_proveedor,cod_familia,cod_tipo_producto):

    django_cursor= connection.cursor()
    cursor= django_cursor.connection.cursor()
    v_salida= cursor.var(cx_Oracle.NUMBER)

    cursor.callproc("PA_GUARDAR_PRODU", [descripcion, fecha_vencimiento,stock,stock_critico,precio,foto,cod_proveedor,cod_familia,cod_tipo_producto,v_salida])
    return v_salida.getvalue()


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
            return redirect(to="listarProducto")
        data['form'] = formulario

    return render(request,'app/producto/modificar.html', data)


def eliminar_Producto(request, id):

    cod_producto = int(id)
    producto = get_object_or_404(Producto, cod_producto = cod_producto)
    producto.delete()
    return redirect(to="listarProducto") 


def agregar_OrdenCompra(request):
    data={
        'form' : AgregarOrdenCompra()
    }

    if request.method == 'POST':
        formulario = AgregarOrdenCompra(data=request.POST)
        if formulario.is_valid():
            print(formulario)
            formulario.save()
            return redirect(to="listarOrdenCompra")
        data['form'] = formulario

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
            return redirect(to="listarOrdenCompra")
        data['form'] = formulario

    return render(request,'app/ordenCompra/modificar.html',data)


def eliminar_ordenCompra(request, id):

    OrdenCompra = get_object_or_404(OrdenesCompra, numorden = id)
    OrdenCompra.delete()
    return redirect(to="listarOrdenCompra")


def agregar_cliente(request):

    data={
        'form': RegistroForm(),
   
    } 
    
    if request.method == 'POST':
        
        formulario = RegistroForm(data = request.POST)
        print(data)
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
            return redirect(to="listarCliente")
        data['form'] = formulario

    return render(request,'app/cliente/modificar.html',data)


def eliminar_Cliente(request, id):

    cliente = get_object_or_404(Cliente, run_cliente = id)
    cliente.delete()
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
    return redirect(to="listarUser")









