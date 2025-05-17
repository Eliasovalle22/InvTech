from django.contrib import admin
from .models import Sede, Dependencia, Salon, Equipo, HistorialCambio


@admin.register(Sede)
class SedeAdmin(admin.ModelAdmin):
    list_display = ('nombre',)
    search_fields = ('nombre',)


@admin.register(Dependencia)
class DependenciaAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'sede')
    list_filter = ('sede',)
    search_fields = ('nombre',)


@admin.register(Salon)
class SalonAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'dependencia')
    list_filter = ('dependencia__sede',)
    search_fields = ('nombre',)


@admin.register(Equipo)
class EquipoAdmin(admin.ModelAdmin):
    list_display = ('serial', 'tipo', 'marca', 'modelo',
                    'dependencia', 'salon', 'asignado_a', 'fecha_instalacion')
    list_filter = ('tipo', 'dependencia', 'salon__dependencia__sede')
    search_fields = ('serial', 'marca', 'modelo', 'asignado_a')
    date_hierarchy = 'fecha_instalacion'



@admin.register(HistorialCambio)
class HistorialCambioAdmin(admin.ModelAdmin):
    list_display = ('equipo', 'fecha', 'descripcion')
    list_filter = ('fecha',)
    search_fields = ('descripcion',)
