from django.shortcuts import render
from django.views.generic.list import ListView
from clientes.models import Cliente

from accounts.views import LoginRequiredMixin

# Create your views here.

class ClienteList(LoginRequiredMixin, ListView):
    model = Cliente

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
