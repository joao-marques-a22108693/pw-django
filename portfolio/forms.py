from django.forms import ModelForm

from .models import Artigo


class ArtigoForm(ModelForm):
    class Meta:
        model = Artigo
        fields = '__all__'
