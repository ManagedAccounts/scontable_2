from django import forms
from django.forms import ModelForm
from productos.models import Producto


class ProductoForm(ModelForm):
    class Meta:
        model = Producto
        fields = ['nombre', 'cproducto', 'tproducto',
                  'tunidad', 'pmarca', 'pcompra', 'pventa',
                  'pimg', 'descripcion']
