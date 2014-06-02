from django.forms import ModelForm
from django import forms

from registrarse.models import Usuario


class RegistroForm(forms.ModelForm):
	class Meta:
		model = Usuario
		