from django.contrib import admin

from .models import *

admin.site.register([Area, Autor, Artigo, Comentario])
