from django.shortcuts import render, redirect
#importamos httpResponse
from django.http import HttpResponse
#importamos las clases de models
from .models import *


# Create your views here.
def home(request):
    deporte = Deporte.objects.all()
    context = {'deporte':deporte}
    return render(request, 'vistas/home.html', context)

def about(request):
    return render(request, 'vistas/about.html')

def products(request, id):
    productos = Productos.objects.filter(tipoDeporte = id)
    deporte = Deporte.objects.get(pk = id)
    context = {'pro':productos, 'dep':deporte}
    return render(request, 'vistas/products.html', context)

def	FormularioContacto(request): 	
 	return render(request,'vistas/register.html')

#CRUD de productos

def listar_productos(request):

    nombreProductos = Productos.objects.all()

	return render(request, 'vistas/listar_productos.html', {
		'nombreProductos':nombreProductos
		})

def eliminar_producto(request, id):
	nombreProductos = nombreProductos.objects.get(id=id)

	try:
		nombreProductos.delete()
		mensaje = "Eliminado correctamente"
	except:
		mensaje ="No se ha podido eliminar"

	return redirect('listar_productos')