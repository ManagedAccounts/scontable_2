from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views.generic.list import ListView
from django.views.generic import View, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.core.urlresolvers import reverse_lazy
from django.core.urlresolvers import reverse
from clientes.models import Cliente
from clientes.forms import ClienteForm

from accounts.views import LoginRequiredMixin

# Create your views here.

class ClienteList(LoginRequiredMixin, ListView):
    model = Cliente

class ClienteCreate(CreateView):
    model = Cliente
    form_class = ClienteForm
    def dispatch(self, *args, **kwargs):
        return super(ClienteCreate, self).dispatch(*args, **kwargs)
    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.request.user
        self.object.save()
        return redirect('clientes:clientes_l')

class ClienteView(View):
    def get(self, request):
        if 'buscar' in request.GET and request.GET['buscar']:
            buscar = request.GET['buscar']
            clientes = Cliente.objects.filter(rod__icontains=buscar)
            # return render(request, 'proveedores/search_results.html',
                # {'proveedores': proveedores, 'query': buscar})
            return render(request, 'clientes/search_result.html',
                {'clientes': clientes, 'query': buscar } )
            #return render(request, 'proveedores/proveedor_list.html', {'error':True})
        else:
            return HttpResponse('Lo sentimos mucho no se encontro el Cliente.')
class ClienteUpdate(UpdateView):
    model = Cliente
    form_class = ClienteForm
    success_url = reverse_lazy("clientes:clientes_l")
    template_name = 'clientes/cliente_update.html'

    def dispatch(self, *args, **kwargs):
        return super(ClienteUpdate, self).dispatch(*args, **kwargs)
"""
class ClienteDelete(DetailView):
    model = Cliente

    def dispatch(self, *args, **kwargs):
        return super(ClienteDelete, self).dispatch(*args, **kwargs)

    def get_success_url(self):
        # To do this because the success_url class variable isn't reversed...
        return reverse('clientes:clientes_l')
"""


























