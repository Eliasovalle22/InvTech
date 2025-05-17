from django.shortcuts import render
from .models import Equipo, Sede, Dependencia, Salon
from django.shortcuts import get_object_or_404
from .forms import HistorialCambioForm
from django.shortcuts import redirect
from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from .models import Perfil
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse





#VISTA LOGIN
def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        usuario = authenticate(request, username=username, password=password)
        if usuario is not None:
            login(request, usuario)
            perfil = Perfil.objects.get(usuario=usuario)
            # Redirección según el rol
            if perfil.rol == 'admin':
                return redirect('dashboard_admin')
            elif perfil.rol == 'tecnico':
                return redirect('dashboard_tecnico')
            elif perfil.rol == 'invitado':
                return redirect('vista_lectura')
        else:
            return render(request, 'inventario/login.html', {'error': 'Credenciales incorrectas'})
    return render(request, 'inventario/login.html')

# VISTAS DE DASHBOARD
@login_required
def dashboard_admin(request):
    return HttpResponse("Bienvenido, administrador")


@login_required
def dashboard_tecnico(request):
    return HttpResponse("Panel del técnico")


@login_required
def vista_lectura(request):
    return HttpResponse("Vista de solo lectura")



def lista_equipos(request):
    sede_id = request.GET.get('sede')
    dependencia_id = request.GET.get('dependencia')
    salon_id = request.GET.get('salon')
    tipo = request.GET.get('tipo')

    equipos = Equipo.objects.all()
    sedes = Sede.objects.all()
    dependencias = Dependencia.objects.all()
    salones = Salon.objects.all()

    if sede_id:
        dependencias = dependencias.filter(sede_id=sede_id)
        salones = salones.filter(dependencia__sede_id=sede_id)
        equipos = equipos.filter(salon__dependencia__sede_id=sede_id)

    if dependencia_id:
        salones = salones.filter(dependencia_id=dependencia_id)
        equipos = equipos.filter(
            dependencia_id=dependencia_id
        ) | equipos.filter(
            salon__dependencia_id=dependencia_id
        )

    if salon_id:
        equipos = equipos.filter(salon_id=salon_id)

    if tipo:
        equipos = equipos.filter(tipo=tipo)

    return render(request, 'inventario/lista_equipos.html', {
        'equipos': equipos.distinct(),
        'sedes': sedes,
        'dependencias': dependencias,
        'salones': salones,
        'filtros': {
            'sede': sede_id,
            'dependencia': dependencia_id,
            'salon': salon_id,
            'tipo': tipo,
        }
    })

# VISTA PARA DETALLE DE EQUIPO


def detalle_equipo(request, equipo_id):
    equipo = get_object_or_404(Equipo, id=equipo_id)
    historial = equipo.cambios.all().order_by('-fecha')

    if request.method == 'POST':
        form = HistorialCambioForm(request.POST)
        if form.is_valid():
            nuevo_cambio = form.save(commit=False)
            nuevo_cambio.equipo = equipo
            nuevo_cambio.usuario = request.user
            nuevo_cambio.save()
            return redirect('detalle_equipo', equipo_id=equipo.id)
    else:
        form = HistorialCambioForm()

    return render(request, 'inventario/detalle_equipo.html', {
        'equipo': equipo,
        'historial': historial,
        'form': form
    })


