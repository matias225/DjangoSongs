from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('canciones/agregar/', views.create, name='cancion_create'),
    path('canciones/editar/<int:id>/', views.update, name='cancion_update'),
    path('canciones/eliminar/<int:id>/', views.delete, name='cancion_delete'),
]
