from django.urls import path
from autos.controlador import controllers
from django.conf.urls import url

urlpatterns = [
    # rutas del mantenedor.
    url(r'^agregarAuto$', controllers.agregarAuto, name="agregarAuto"),

    # Ruta para la pagina de inicio
    url(r'^$', controllers.index, name="inicio"),
    url(r'^modificarAuto/(?P<pk>\d+)/$',
        controllers.modificarAuto,
        name="modificarAuto"),
    url(r'^eliminarAuto/(?P<pk>\d+)/$',
        controllers.eliminarAuto,
        name="eliminarAuto"),
    url(r'^verAuto/(?P<pk>\d+)/$',
        controllers.verAuto,
        name="verAuto"),
]
