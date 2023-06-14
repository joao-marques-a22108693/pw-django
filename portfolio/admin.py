from django.contrib import admin

from .models import *

admin.site.register([Area, Artigo, Autor, Cadeira, Comentario, Pessoa, Projeto])
