from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render_to_response

def comentar(request):
	return render_to_response('comentario.html')