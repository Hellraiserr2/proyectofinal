from django.shortcuts import render,redirect
from .models import Usuario,Producto
from django.http import HttpResponseRedirect
from django.forms import ModelForm
from .forms import UsuarioForm

from .forms import UsuarioForm
# Create your views here.
def index(request):
    context={}
    return render(request,'alumnos/index.html', context)

#vista del carro
def carroCompra(request):
    context={}
    return render(request, 'alumnos/carroDeCompras.html', context)

#vista de los datos del producto
def compraDatos(request):
    context={}
    return render(request,'alumnos/compraDatos.html', context)

#vista de la pagina de exteriores
def exteriores(request):
    context={}
    return render(request,'alumnos/exteriores.html', context)

#vista del formulario de subscripcion premium
def formularioSubscripcion(request):
    context={}
    return render(request,'alumnos/formularioSub.html',context)
#vista de la pagina del maule
def paginaMaule(request):
    context={}
    return render(request,'alumnos/maule.html', context)

#vista en proceso
def pagPlantas(request):
    context={}
    return render(request,'alumnos/pagPlantas.html',context)

#a
def producto_1_informacion(request):
    producto=Producto.objects.all()
    context={'producto':producto}
    return render(request,'alumnos/producto_1_informacion.html',context)


#Crud de usuarios
def crearCuenta(request):
    if request.method == "POST":
        form = UsuarioForm(request.POST)
        if form.is_valid():
            form.save()
            form=UsuarioForm()
            context={'mensaje':"datos ingresados","form":form}
            return render(request,'alumnos/crearCuenta.html', context)
        else:
            context = {'form':form}
            return render(request,'alumnos/crearCuenta.html',context)
    else:
        form = UsuarioForm()
        context={'form':form}
        return render(request,'alumnos/crearCuenta.html', context)

def tablaProd(request):
    producto = Producto.objects.all()
    context={'productos':producto}
    return render(request,'alumnos/tablaProd.html', context)

def mostrar_productos(request):
    producto = Producto.objects.all()
    context={'productos':producto}
    return render(request, 'alumnos/tablaProd.html', context)


def eliminarProd(request, pk):
    context = {}
    try:
        producto = Producto.objects.get(nombreProducto=pk)
        producto.delete()
        mensaje = "Producto eliminado..."
        productos = Producto.objects.all()
        context = {'productos': productos, 'mensaje': mensaje}  
    except Producto.DoesNotExist:
        mensaje = "Error: Producto no existente..."
        productos = Producto.objects.all()
        context = {'productos': productos, 'mensaje': mensaje} 
    return render(request, 'alumnos/tablaProd.html', context)



