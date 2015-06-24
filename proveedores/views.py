from django.shortcuts import render
from django.views.generic.list import ListView
from proveedores.models import Proveedor

from accounts.views import LoginRequiredMixin

# Create your views here.i

class ProveedorList(LoginRequiredMixin, ListView):
    model = Proveedor
