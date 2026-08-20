from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path(
        'canciones/agregar/',
        views.create,
        name='cancion_create'
    ),
]
