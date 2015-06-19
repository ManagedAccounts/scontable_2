from django.shortcuts import render, render_to_response, get_object_or_404
from .models import Comprobante, Cliente, Detalle
from django.http import HttpResponse, HttpResponseRedirect
from django.template import RequestContext
from eventos.forms import ComprobanteForm, ClienteForm, DetalleForm


def Comprobante(request):
    comprobante = Comprobante.objects.all()
    titulo = "registro de comprobantes "
    return render_to_response('ventas/comprobante.html', {
        'comprobante':comprobante,'titulo':titulo},
         context_instance=RequestContext(request))

def comprar(request):
    if request.method == 'POST':
        formulario = ComprobanteForm(request.POST, request.FILE)
        if formulario.is_valid():
            formulario.save()
            return HttpResponseRedirect('/comprobante')
    else:
        formulario = ComprobanteForm()
    return render_to_response('ventas/comprobanteform.html',
                              {'formulario':formulario},
                          context_instance=RequestContext(request))


def comprobante_edit (request, id):
        comprobante_edit= Comprobante.objects.get(pk=id)
        if request.method == 'POST':
            formulario = ComprobanteForm(request.POST, instance = comprobante_edit)
            if formulario.is_valid():
                formulario.save()
                return HttpResponseRedirect("/comprobante")
        else:
            formulario = ComprobanteForm(instance= comprobante_edit)
        return render_to_response('ventas/comprobanteEdit.html',
                                 {'formulario': formulario},
                                  context_instance = RequestContext(request))
def comprobante_borrar (request, id):
    comprobante_borrar = get_object_or_404(Comprobante, pk=id)
    comprobante_borrar.delete()
    return HttpResponseRedirect("/comprobante")


def clientes(request):
    cliente = Cliente.objects.all()
    titulo = "registro de clientes "
    return render_to_response('ventas/clientes.html', {
        'cliente':cliente,'titulo':titulo},
         context_instance=RequestContext(request))

def cliente_add(request):
    if request.method == 'POST':
        formulario = ClienteForm(request.POST, request.FILE)
        if formulario.is_valid():
            formulario.save()
            return HttpResponseRedirect('/clientes')
    else:
        formulario = ClienteForm()
    return render_to_response('ventas/clienteform.html',
                              {'formulario':formulario},
                          context_instance=RequestContext(request))


def cliente_edit (request, id):
        cliente_edit= Cliente.objects.get(pk=id)
        if request.method == 'POST':
            formulario = clienteForm(request.POST, instance = cliente_edit)
            if formulario.is_valid():
                formulario.save()
                return HttpResponseRedirect("/clientes")
        else:
            formulario = ClienteForm(instance= cliente_edit)
        return render_to_response('ventas/clienteEdit.html',
                                 {'formulario': formulario},
                                  context_instance = RequestContext(request))
def cliente_borrar (request, id):
    cliente_borrar = get_object_or_404(Cliente, pk=id)
    clientee_borrar.delete()
    return HttpResponseRedirect("/clientes")






