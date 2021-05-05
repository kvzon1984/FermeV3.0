from django.shortcuts import render
from django.shortcuts import redirect
from .forms import RegistroForm,UserPass


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