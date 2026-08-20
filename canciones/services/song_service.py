from canciones.models import Cancion

def obtener_todas():
    return Cancion.objects.all().order_by('id')


def crear_cancion(datos):
    return Cancion.objects.create(
        titulo=datos['titulo'],
        artista=datos['artista'],
        popularidad=datos['popularidad'],
    )
