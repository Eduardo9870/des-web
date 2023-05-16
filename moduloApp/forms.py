from django import forms
from django.forms import ModelForm
from django.core import validators
from django.core.validators import RegexValidator
from moduloApp.models import *


class tipoProductoForm (forms.Form):
    tipoProducto = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'form-control'}))
    descripcionTipoProducto = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'form-control'}))


class ProductoForm (forms.Form):
    nombreProducto = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'form-control'}))
    cantidad = forms.IntegerField(
        widget=forms.NumberInput(attrs={'class': 'form-control'}))
    descripcionProducto = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'form-control'}))


class ClienteForm (forms.Form):
    nombreCliente = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'form-control'}))
    telefonoCliente = forms.IntegerField(
        widget=forms.NumberInput(attrs={'class': 'form-control'}))
    correo = forms.EmailField(widget=forms.EmailInput(
        attrs={'class': 'form-control'}))


class ProyectoForm (forms.Form):
    nombreProyecto = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'form-control'}))
    descripcionProyecto = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'form-control'}))
    estadoProyecto = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'form-control'}))


class Bodega (forms.Form):
    nombreBodega = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'form-control'}))
    direccionBodega = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'form-control'}))


class productoBodegaForm (forms.Form):
    stock = forms.IntegerField(
        widget=forms.NumberInput(attrs={'class': 'form-control'}))
