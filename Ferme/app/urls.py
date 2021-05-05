from django.urls import path
from .views import home,registro,userPass


urlpatterns = [
    path('', home, name="home"),
    path('registro/', registro, name="registro"),
    path('userPass/', userPass, name="userPass" )
]
