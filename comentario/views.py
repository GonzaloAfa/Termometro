from django.shortcuts import render

from django.shortcuts import render_to_response, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.template import RequestContext

from preguntar.models import Pregunta 
from comentario.models import Comentario

#Return with json
from django.core import serializers

import json

def comentar(request): 
	question_id = request.GET.get('id')
	query_pregunta = get_object_or_404(Pregunta, pk = question_id)
	query_comentarios = Comentario.objects.filter(id_pregunta = query_pregunta)
	success = 'NOT' 

	if request.method == "POST":
		usuario 	= request.POST.get("nombre","")
		texto		= request.POST.get("comentario","")

		comentario = Comentario(usuario=usuario, texto=texto, id_pregunta=query_pregunta)
		comentario.save()
		success = 'OK'


	return render_to_response('comentario-v2.html',
		{'modelo': query_pregunta, 'comentarios':query_comentarios, 'success':success },
		context_instance=RequestContext(request))



def comentar_experimento(request): 
	question_id = request.GET.get('id')
	query_pregunta = get_object_or_404(Pregunta, pk = question_id)
	query_comentarios = Comentario.objects.filter(id_pregunta = query_pregunta).reverse()
	success = 'NOT' 

	if request.method == "POST":
		usuario 	= request.POST.get("nombre","")
		texto		= request.POST.get("comentario","")

		comentario = Comentario(usuario=usuario, texto=texto, id_pregunta=query_pregunta)
		comentario.save()
		success = 'OK'


	return render_to_response('comentario-v1.html',
		{'modelo': query_pregunta, 'comentarios':query_comentarios, 'success':success },
		context_instance=RequestContext(request))



def votar_pregunta(request):
	if request.is_ajax:

		if request.method== 'GET':

			question_id 	= request.GET.get('question_id') #TODO: verificar que sea Int
			option 			= request.GET.get('option') 


			query_pregunta = get_object_or_404(Pregunta, pk = question_id)


			if (option == "positivo"):
				query_pregunta.voto_positivo 	= query_pregunta.voto_positivo + 1
			elif (option == "neutro"):
				query_pregunta.voto_neutro 		= query_pregunta.voto_neutro + 1
			elif (option == "negativo"):
				query_pregunta.voto_negativo	= query_pregunta.voto_negativo + 1

			query_pregunta.save()


			preguntas = Pregunta.objects.filter(id=question_id)
			data = serializers.serialize('json', preguntas, 
				fields=('pk','voto_positivo','voto_neutro', 'voto_negativo'))
			
			return HttpResponse(data, mimetype='application/json')


		else:
			return HttpResponse(status=400)
	else:
		return HttpResponse(status=501)



def lista_preguntas(request):
	lista_preguntas = Pregunta.objects.all().reverse()
	return render_to_response('preguntas.html', 
		{'lista_preguntas' : lista_preguntas}, 
		context_instance=RequestContext(request))
