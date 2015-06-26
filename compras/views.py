from django.shortcuts import render
from django.views.generic.list import ListView
from compras.models import Ordencompra

# Create your views here.

class OrdencompraList(ListView):
    model = Ordencompra


