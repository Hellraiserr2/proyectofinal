from django.contrib import admin

# Register your models here.
from .models import Planta, Categoria

# Registra el modelo Planta en el sitio de administración
@admin.register(Planta)
class PlantaAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'categoria', 'precio')  # Campos a mostrar en la lista de objetos
    list_filter = ('categoria',)  # Filtros disponibles en la lista
    search_fields = ('nombre', 'descripcion')  # Campos de búsqueda
    prepopulated_fields = {'slug': ('nombre',)}  # Genera el slug automáticamente

# Registra el modelo Categoria en el sitio de administración
@admin.register(Categoria)
class CategoriaAdmin(admin.ModelAdmin):
    list_display = ('nombre',)  # Campos a mostrar en la lista de objetos
    search_fields = ('nombre',)  # Campos de búsqueda