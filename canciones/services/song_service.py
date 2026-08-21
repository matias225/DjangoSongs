from canciones.models import Cancion

def obtener_todas():
    return Cancion.objects.all().order_by('id')

def crear_cancion(datos):
    return Cancion.objects.create(titulo=datos['titulo'], artista=datos['artista'], popularidad=datos['popularidad'],)

def obtener_por_id(id):
    return Cancion.objects.get(id=id)

def actualizar_cancion(id, datos):
    cancion = obtener_por_id(id)

    cancion.titulo = datos['titulo']
    cancion.artista = datos['artista']
    cancion.popularidad = datos['popularidad']

    cancion.save()
    return cancion

def eliminar_cancion(id):
    cancion = obtener_por_id(id)
    cancion.delete()
