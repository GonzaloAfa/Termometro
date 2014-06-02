from django.contrib import admin

from preguntar.models import Pregunta, Categoria


admin.site.register(Pregunta)
admin.site.register(Categoria)