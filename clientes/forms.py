from django import forms
from django.forms import ModelForm
from clientes.models import Cliente

class ClienteForm(ModelForm):
    class Meta:
        model = Cliente
        fields = ['rsocial', 'tcliente', 'rod', 'direccion', 'toc', 'estado']
