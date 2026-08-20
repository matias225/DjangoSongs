from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator

# Create your models here.
class Cancion(models.Model):
    titulo = models.CharField(
        max_length=200,
        null=False,
        blank=False
    )

    artista = models.CharField(
        max_length=150,
        null=False,
        blank=False
    )

    popularidad = models.IntegerField(
        null=False,
        blank=False,
        validators=[
            MinValueValidator(1),
            MaxValueValidator(10)
        ]
    )

    class Meta:
        db_table = 'cancion'
        verbose_name = 'Canción'
        verbose_name_plural = 'Canciones'

    def __str__(self):
        return f'{self.titulo} - {self.artista}'
