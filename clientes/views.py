from django.shortcuts import render, redirect
from django.views.generic.list import ListView
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

"""
def clientesearch(request):
    error = False
    if 'w' in request.GET:
        w = request.GET['w']
        if not w:
            error = True
        else:
            clientes = Cliente.objects.filter(rod__icontains=w)
            return render(request, 'clientes/cliente_list.html',
                          {'clientes:': clientes, 'result':w})
    return render(request,'clientes/cliente_search.html', {'error': True})
"""
