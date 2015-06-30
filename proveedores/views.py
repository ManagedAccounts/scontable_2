from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views.generic.list import ListView
from django.views.generic import View
from django.views.generic.edit import CreateView
from proveedores.models import Proveedor
from proveedores.forms import ProveedorForm

from accounts.views import LoginRequiredMixin

# Create your views here.i

class ProveedorList(LoginRequiredMixin, ListView):
    model = Proveedor

class ProveedorCreate(CreateView):
    model = Proveedor
    form_class = ProveedorForm
    def dispatch(self, *args, **kwargs):
        return super(ProveedorCreate, self).dispatch(*args, **kwargs)
    def form_valid(self, form):
        self.object = form.save(commit=False)
        # self.object.owner = self.request.user
        self.object.save()
        return redirect('proveedores:proveedor_l')

class ProveedorView(View):
    def get(self, request):
        if 'buscar' in request.GET and request.GET['buscar']:
            buscar = request.GET['buscar']
            proveedores = Proveedor.objects.filter(rod__icontains=buscar)
            return render(request, 'proveedores/search_result.html',
                {'proveedores': proveedores, 'query': buscar } )
        else:
            return HttpResponse('Lo sentimos mucho no se encontro el Proveedor.')

