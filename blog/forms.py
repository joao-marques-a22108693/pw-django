from django.forms import ModelForm
from .models import Autor, Artigo


class AutorForm(ModelForm):
    class Meta:
        model = Autor
        fields = '__all__'
