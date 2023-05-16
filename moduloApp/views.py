from django.shortcuts import render, redirect
from moduloApp.models import *
from moduloApp.forms import *
from django.contrib.auth.views import LoginView
# Create your views here.


def index(request):
    return render(request, 'sistema/index.html')


def vistaDos(request):
    return render(request, 'sistema/segunda.html')


def viewProducto(request):
    producto = Producto.objects.all()
    data = {
        'tipo': producto,
        'titulo': 'Productos',
    }
    return render(request, 'sistema/viewProductos.html', data)


def addProducto(request):
    data = {
        'titulo': 'Productos',
        'form': ProductoForm()
    }
    if (request.method) == 'POST':
        formulario = ProductoForm(request.POST)
        if formulario.is_valid():
            formulario.save()
            return redirect('/producto')
        else:
            data['form'] = formulario
    return render(request, 'sistema/formProductos.html', data)


def deleteProducto(request, id):
    producto = Producto.objects.get(id=id)
    producto.delete()
    return redirect('/producto')


def editarProducto(request, id):
    form = Producto.objects.get(id=id)
    data = {
        'titulo': 'Editar productos',
        'form': ProductoForm(instance=form)
    }
    if (request.method == 'POST'):
        form = ProductoForm(request.POST, instance=form)
        if (form.is_valid()):
            form.save()
            return redirect('/producto')
        else:
            data['form'] = form
    return render(request, 'sistema/formProductos.html', data)


class CustomLoginView(LoginView):
    template_name = 'sistema/login.html'
