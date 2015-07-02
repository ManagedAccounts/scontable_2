from django.shortcuts import render, redirect
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
#from django.views.generic.form import FormView
from django.core.urlresolvers import reverse_lazy
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from compras.models import Ordencompra
from compras.forms import OrdencompraForm

from accounts.views import LoginRequiredMixin

class OrdencompraList(LoginRequiredMixin, ListView):
    model = Ordencompra

class OrdencompraCreate(LoginRequiredMixin, CreateView):
    model = Ordencompra
    form_class = OrdencompraForm
    @method_decorator(login_required(login_url = "login"))

    def dispatch(self, *args, **kwargs):
        return super(OrdencompraCreate, self).dispatch(*args, **kwargs)
    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.save()
        return redirect('compras:compras_l')
