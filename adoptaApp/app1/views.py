from django.shortcuts import render
from .models import *
from django.http import HttpResponseRedirect, HttpResponse, JsonResponse, FileResponse
from django.urls import reverse
from datetime import datetime
from django.contrib.auth.decorators import login_required

# Create your views here.
def ingreso(request):
    return render(request,'ingresoUsuario.html')

def registro(request):
    return render(request,'registroUsuario.html')

@login_required(login_url='/')
def home(request):
    tipos = TipoMascota.objects.all()
    mascotas = Mascota.objects.all()
    return render(request,'home.html',{
        'tipos':tipos,
        'mascotas':mascotas
    })

def crearTipo(request):
    if request.method == 'POST':
        nombre = request.POST.get('nombre')
        descripcion = request.POST.get('descripcion')
        TipoMascota.objects.create(
            nombre=nombre,
            descripcion=descripcion
        )
        return HttpResponseRedirect(reverse('app1:home'))
    tipos = TipoMascota.objects.all()
    return render(request,'crearTipo.html',{
        'tipos':tipos
    })

def crearMascota(request):
    if request.method == 'POST':
        nombre = request.POST.get('nombre')
        edad = request.POST.get('edad')
        descripcion = request.POST.get('descripcion')
        idTipo = request.POST.get('tipo')
        foto = request.FILES.get('foto')
        tipo = TipoMascota.objects.get(id=idTipo)
        Mascota.objects.create(
            nombre=nombre,
            edad=edad,
            descripcion=descripcion,
            foto=foto,
            tipo=tipo,
            estado='Disponible'
        )
        return HttpResponseRedirect(reverse('app1:home'))
    tipos = TipoMascota.objects.all()
    return render(request,'crearMascota.html',{
        'tipos':tipos
    })

def mascotasxtipo(request,idTipo):
    tipos = TipoMascota.objects.all()
    tipo = TipoMascota.objects.get(id=idTipo)
    mascotas = Mascota.objects.filter(tipo=tipo)
    return render(request,'home.html',{
        'tipos':tipos,
        'mascotas':mascotas,
        'tipo_seleccionado':tipo
    })

def detalleMascota(request,idMascota):
    mascota = Mascota.objects.get(id=idMascota)
    tipos = TipoMascota.objects.all()
    adopcion = None

    if mascota.estado == 'Adoptado':
        try:
            adopcion = Adopcion.objects.get(mascota=mascota)
        except Adopcion.DoesNotExist:
            adopcion = None
    
    if request.method == 'POST' and mascota.estado == 'Disponible':
        nombre = request.POST.get('nombre')
        email = request.POST.get('email')
        telefono = request.POST.get('telefono')

        persona = Persona.objects.create(
            nombre=nombre,
            email=email,
            telefono=telefono
        )

        Adopcion.objects.create(
            mascota=mascota,
            persona=persona,
            fecha_adopcion=datetime.now().strftime("%d/%m/%Y %H:%M")
        )

        mascota.estado = 'Adoptado'
        mascota.save()
        return HttpResponseRedirect(reverse('app1:detalleMascota', args=[mascota.id]))

    return render(request,'detalleMascota.html',{
        "tipos":tipos,
        "adopcion": adopcion,
        "mascota":mascota,
    })


def listaAdoptantes(request):
    tipos = TipoMascota.objects.all()
    return render(request,'listaAdoptantes.html',{
        'tipos':tipos
    })