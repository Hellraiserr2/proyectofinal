from django.urls import path
from . import views

urlpatterns=[
    path('index.html', views.index, name='index'),
    path('carroDeCompras.html', views.carroCompra, name='carroCompra'),
    path('crearCuenta.html', views.crearCuenta, name='crearCuenta'),
    path('compraDatos.html', views.compraDatos, name='compraDatos'),
    path('exteriores.html', views.exteriores, name='exteriores'),
    path('formularioSub.html', views.formularioSubscripcion, name='formularioSub'),
    path('paginaMaule.html', views.paginaMaule, name='paginaMaule'),
    path('pagPlantas.html', views.pagPlantas, name='pagPlantas'),
    path('producto_1_informacion.html',views.producto_1_informacion, name='producto_1_informacion')
]