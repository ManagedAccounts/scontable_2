from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views.generic.list import ListView
from django.views.generic import View
from django.views.generic.edit import CreateView, UpdateView, DeleteView
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

