from django.shortcuts import redirect, render, render_to_response
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader, RequestContext
from autos.formularios.forms import nuevoAutoForm, filtrarAutosForm
from autos.modelo.models import Automovil, Busqueda
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator


# Vista de la pagina de inicio.
def index(request):
    if request.method == 'POST':
        form = filtrarAutosForm(request.POST)
    else:
        form = filtrarAutosForm()
    plantilla = loader.get_template("index.html")
    contexto = {'form': form, 'autos': __aplicarFiltro(request, form)}
    return HttpResponse(plantilla.render(contexto, request))


# Funcion para aplicar el filtro de la busqueda.
def __aplicarFiltro(request, form):
    if form.is_valid():
        filtro = Busqueda()
        filtro.marca = request.POST['marca']
        if filtro.marca == 'Todos':
            misAutos = Automovil.objects.all()
        else:
            misAutos = Automovil.objects.filter(marca=filtro)
    else:
        misAutos = Automovil.objects.all()
    return __paginarResultados(request, misAutos, 10)


# Funcion para paginar resultados.
def __paginarResultados(request, lista, elemPorPagina):
    miPaginador = Paginator(lista, elemPorPagina)
    page = request.GET.get('page')
    return miPaginador.get_page(page)


# Agregar un nuevo automovil
def agregarAuto(request):
    if request.method == "POST":
        form = nuevoAutoForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            miAuto = Automovil(
                marca=data.get('marca'),
                modelo=data.get('modelo'),
                puertas=data.get('puertas'),
                anio=data.get('anio'),
                descripcion=data.get('descripcion'))
            miAuto.save()
            return redirect('inicio')
    else:
        form = nuevoAutoForm()
    return render(request, "agregar.html", {'form': form})


# modificar informacion del automovil.
def modificarAuto(request, pk):
    if request.method == "POST":
        form = nuevoAutoForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            miAuto = Automovil.objects.get(id=pk)
            miAuto.marca=data.get('marca')
            miAuto.modelo = data.get('modelo')
            miAuto.puertas= data.get('puertas')
            miAuto.anio=data.get('anio')
            miAuto.descripcion=data.get('descripcion')
            miAuto.save()
            return redirect('inicio')
    else:
        miAuto = Automovil.objects.get(id=pk)
        form = nuevoAutoForm(instance=miAuto)
    return render(request, "agregar.html", {'form': form})


# Eliminar automovil
def eliminarAuto(request, pk):
    miAuto = Automovil.objects.get(id=pk).delete()
    return redirect('inicio')


# vista para mostrar la informacion del automovil.
def verAuto(request, pk):
    miAuto = Automovil.objects.get(id=pk)
    plantilla = loader.get_template("info.html")
    contexto = {'auto': miAuto}
    return HttpResponse(plantilla.render(contexto, request))
