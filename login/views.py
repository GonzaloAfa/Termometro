from django.shortcuts import render_to_response,redirect,render
from django.template import RequestContext
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout as auth_logout, login
from social.apps.django_app.utils import strategy
from django.http import HttpResponse
# Create your views here.
def prueba(request):
    return render_to_response('login_test.html', RequestContext(request))