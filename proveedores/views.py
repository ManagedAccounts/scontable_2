from django.shortcuts import render
from django.views.generic.list import ListView
from proveedores.models import Proveedor

# Create your views here.i

class ProveedorList(ListView):
    model = Proveedor
