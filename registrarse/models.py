from django.db import models


class Usuario(models.Model):
	nombre 		= models.CharField(max_length=30)
	apellido 	= models.CharField(max_length=30)
	email 		= models.EmailField()
	fecha 		= models.DateTimeField(auto_now=True)
	nick 		= models.CharField(max_length=15)

	def __unicode__(self):
		return self.nombre + " " + self.apellido