from django.shortcuts import render
from django.http import HttpResponse, JsonResponse, FileResponse, HttpResponseRedirect

# Create your views here.

def home(request):
    return HttpResponse('Esta es mi primera ruta en django')

def saludo(request):
    return HttpResponse('Saludando desde la ruta /saludo')

def hola(request):
    mascotas = ['Luna','Dovi','Balto','Ayudante de santa']
    return render(request,'hola.html',{
        'nombre': 'Luis',
        'mascotas':mascotas
    })