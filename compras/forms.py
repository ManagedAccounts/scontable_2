from django import forms
from django.forms import ModelForm
from compras.models import Ordencompra

class OrdencompraForm(ModelForm):
    class Meta:
        model = Ordencompra
        fields = ['tcomprobante', 'ccompra', 'pcompra',
                  'aproucto', 'tpago', 'fecha', 'descripcion',
                  'cantidad', 'uprecio']
