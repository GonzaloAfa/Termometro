from django.db import models

from registrarse.models import Usuario

class Categoria(models.Model):
	tipo		= models.CharField(max_length=30)

	def __unicode__(self):
		return self.tipo


# Create your models here.
class Pregunta(models.Model):
	usuario 	= models.ForeignKey(Usuario)	
	texto 		= models.TextField()
	categoria 	= models.ManyToManyField(Categoria) 
	relevancia 	= models.IntegerField(default=0)
	fecha 		= models.DateTimeField(auto_now = True)

	def __unicode__(self):
		return self.texto