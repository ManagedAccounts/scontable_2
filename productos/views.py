from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView
from django.views.generic.list import ListView
from productos.models import Producto
from productos.forms import ProductoForm

from accounts.views import LoginRequiredMixin
# Create your views here.
class ProductoList(LoginRequiredMixin, ListView):
    model = Producto

class ProductoCreate(LoginRequiredMixin, CreateView):
    model = Producto
    form_class = ProductoForm
    def dispatch(self, *args, **kwargs):
        return super(ProductoCreate, self).dispatch(*args, **kwargs)
    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.save()
        self.request.user
        # return redirect(self.object)
        return redirect('productos:productos_l')
