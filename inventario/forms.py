from django import forms
from .models import HistorialCambio


class HistorialCambioForm(forms.ModelForm):
    class Meta:
        model = HistorialCambio
        fields = ['descripcion']
        widgets = {
            'descripcion': forms.Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Ej: Se cambió el disco duro de 500GB por uno SSD de 256GB',
                'rows': 3
            }),
        }
        labels = {
            'descripcion': 'Detalle del cambio realizado'
        }