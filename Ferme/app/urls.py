from django.urls import path
from .views import home,registro,userPass, agregarProducto, agregarEmpleado


urlpatterns = [
    path('', home, name="home"),
    path('registro/', registro, name="registro"),
    path('userPass/', userPass, name="userPass" ),
    path('agregarProducto/', agregarProducto, name="agregarProducto"),
    path('agregarEmpleado/',agregarEmpleado,name='agregarEmpleado')

]
