from django.urls import path, include
from . import views

app_name = 'app1'

urlpatterns = [
    path('', views.home, name='home'),
    path('saludo',views.saludo,name='saludo'),
    path('hola',views.hola,name='hola')
]