from django.forms import ModelForm

from .models import Artigo, Comentario


class ArtigoForm(ModelForm):
    class Meta:
        model = Artigo
        fields = '__all__'


class ComentarioForm(ModelForm):
    class Meta:
        model = Comentario
        fields = ['autor', 'texto']
