from django.shortcuts import render

# Create your views here.
def index(request):
    context={}
    return render(request,'alumnos/index.html', context)

#vista del carro
def carroCompra(request):
    context={}
    return render(request, 'alumnos/carroDeCompras.html', context)

#vista del formulario de creacion de cuenta
def crearCuenta(request):
    context={}
    return render(request,'alumnos/crearCuenta.html', context)

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
    context={}
    return render(request,'alumnos/producto_1_informacion',context)
