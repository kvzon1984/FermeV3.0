from django.shortcuts import render
from django.shortcuts import redirect
from .forms import RegistroForm,UserPass,AgregarProductoForm,AgregarEmpleadoForm


# Create your views here.


def home(request):

    return render(request, 'app/home.html')


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
    return render(request,'app/producto/agregarProducto.html',data)

def agregarEmpleado(request):

    data={
        'form' : AgregarEmpleadoForm()
    }

    if request.method == 'POST':
        formulario = AgregarEmpleadoForm(data=request.POST)
        if formulario.is_valid():
            formulario.save()
            return redirect(to="login")
        data['form'] = formulario


    return render(request,'app/empleado/agregarEmpleado.html',data)