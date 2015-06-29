from django.shortcuts import render, redirect
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
#from django.views.generic.form import FormView
from compras.models import Ordencompra
from compras.forms import OrdencompraForm

# Create your views here.

class OrdencompraList(ListView):
    model = Ordencompra

class OrdencompraCreate(CreateView):
    model = Ordencompra
    form_class = OrdencompraForm
    def dispatch(self, *args, **kwargs):
        return super(OrdencompraCreate, self).dispatch(*args, **kwargs)
    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.save()
        return redirect('compras:compras_l')
