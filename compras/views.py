from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
#from django.views.generic.form import FormView
from compras.models import Ordencompra

# Create your views here.

class OrdencompraList(ListView):
    model = Ordencompra


