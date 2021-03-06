from django.db import models
from registrarse.models import Usuario
from preguntar.models import Pregunta

class Comentario(models.Model):
	usuario 	= models.CharField(max_length=15)
	texto		= models.TextField()
	fecha		= models.DateTimeField(auto_now=True)
	id_pregunta = models.ForeignKey(Pregunta)
	relevancia	= models.IntegerField(default=0)

	