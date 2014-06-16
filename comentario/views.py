from django.shortcuts import render
from django.http import HttpResponse
from django.template import RequestContext
from django.shortcuts import render_to_response, get_object_or_404

from preguntar.models import Pregunta 
from comentario.models import Comentario


def comentar(request, id): 
	query_pregunta = get_object_or_404(Pregunta, pk = id)
	query_comentarios = Comentario.objects.filter(id_pregunta = query_pregunta)

	if request.method == "POST":
		usuario 	= request.POST.get("nombre","")
		texto		= request.POST.get("comentario","")

		comentario = Comentario(usuario=usuario, texto=texto,
		 id_pregunta=query_pregunta)

		comentario.save()

	return render_to_response('comentario.html',
		{'modelo': query_pregunta, 'comentarios':query_comentarios},
		context_instance=RequestContext(request))


def lista_preguntas(request):
	lista_preguntas = Pregunta.objects.all()
	return render_to_response('preguntas.html', 
		{'lista_preguntas' : lista_preguntas}, 
		context_instance=RequestContext(request))
