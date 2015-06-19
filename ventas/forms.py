# coding:utf-8
from django.forms import ModelForm
from django import forms
from .models import Comprobante, Cliente, Detalle

class ComprobanteForm(ModelForm):
     class Meta:
         model = Comprobante

class ClienteForm(ModelForm):
     class Meta:
         model = Cliente

class DetalleForm(ModelForm):
     class Meta:
         model = Detalle

