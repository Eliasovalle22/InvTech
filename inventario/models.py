
from django.db import models
from django.contrib.auth.models import User

class Sede(models.Model):
    nombre = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre


class Dependencia(models.Model):
    nombre = models.CharField(max_length=100)
    sede = models.ForeignKey(Sede, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.nombre} - {self.sede}"


class Salon(models.Model):
    nombre = models.CharField(max_length=100)
    dependencia = models.ForeignKey(Dependencia, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.nombre} - {self.dependencia}"


class Equipo(models.Model):
    TIPO_CHOICES = [
        ('PC', 'Computador'),
        ('LT', 'Portátil'),
    ]

    tipo = models.CharField(max_length=2, choices=TIPO_CHOICES)
    marca = models.CharField(max_length=100)
    modelo = models.CharField(max_length=100)
    serial = models.CharField(max_length=100, unique=True)
    procesador = models.CharField(max_length=100)
    ram = models.CharField(max_length=50)
    disco_duro = models.CharField(max_length=50)
    sistema_operativo = models.CharField(max_length=100)
    salon = models.ForeignKey(Salon, on_delete=models.SET_NULL, null=True, blank=True)
    dependencia = models.ForeignKey('Dependencia', on_delete=models.SET_NULL, null=True, blank=True)
    asignado_a = models.CharField(max_length=100, blank=True)
    fecha_compra = models.DateField(null=True, blank=True)
    fecha_instalacion = models.DateField(null=True, blank=True)

    def __str__(self):
        return f"{self.tipo} - {self.serial}"


class HistorialCambio(models.Model):
    equipo = models.ForeignKey(
        Equipo,
        on_delete=models.CASCADE,
        related_name='cambios'
    )
    descripcion = models.TextField()
    fecha = models.DateField(auto_now_add=True)
    usuario = models.ForeignKey(
        User, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return f"{self.equipo} - {self.fecha}"


class Perfil(models.Model):
    ROLES = (
        ('admin', 'Administrador'),
        ('tecnico', 'Técnico'),
        ('invitado', 'Invitado'),
    )

    usuario = models.OneToOneField(User, on_delete=models.CASCADE)
    rol = models.CharField(max_length=20, choices=ROLES)

    def __str__(self):
        return f'{self.usuario.username} - {self.get_rol_display()}'
