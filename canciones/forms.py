from django import forms
from .models import Cancion

class CancionForm(forms.ModelForm):

    class Meta:
        model = Cancion
        fields = ['titulo', 'artista', 'popularidad',]
        labels = {'titulo': 'Título', 'artista': 'Artista', 'popularidad': 'Popularidad',}

        widgets = {
            'titulo': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Ej: Bohemian Rhapsody',
                }
            ),

            'artista': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Ej: Queen',
                }
            ),

            'popularidad': forms.NumberInput(
                attrs={
                    'class': 'form-control',
                    'min': 1,
                    'max': 10,
                    'placeholder': '1 - 10',
                }
            ),
        }

    def clean_titulo(self):
        titulo = self.cleaned_data['titulo'].strip()

        if not titulo:
            raise forms.ValidationError(
                'El título es obligatorio.'
            )

        return titulo

    def clean_artista(self):
        artista = self.cleaned_data['artista'].strip()

        if not artista:
            raise forms.ValidationError(
                'El artista es obligatorio.'
            )

        return artista
