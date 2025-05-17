"""
URL configuration for inventario_tecnologico project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from inventario import views

urlpatterns = [
    path('admin/', admin.site.urls),
    
    ## URL para la vista de lista de equipos
    path('equipos/', views.lista_equipos, name='lista_equipos'),
    
    ## URL para la vista de detalle de un equipo
    path('equipos/<int:equipo_id>/', views.detalle_equipo, name='detalle_equipo'),
    
    path('login/', views.login_view, name='login'),
    path('admin/dashboard/', views.dashboard_admin, name='dashboard_admin'),
    path('tecnico/dashboard/', views.dashboard_tecnico, name='dashboard_tecnico'),
    path('vista/', views.vista_lectura, name='vista_lectura'),

]
