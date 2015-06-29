from django import forms
from django.forms import ModelForm
from proveedores.models import Proveedor


class ProveedorForm(ModelForm):
    class Meta:
        model = Proveedor
        fields = ['rsocial', 'rod', 'direccion', 'toc', 'email',
                  'contacto', 'descripcion']
