from django.shortcuts import render
from django.http import HttpResponse
from django.template import RequestContext
from django.shortcuts import render_to_response

def comentar(request):
	return render_to_response('comentario.html', context_instance=RequestContext(request))