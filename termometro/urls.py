from django.conf.urls import patterns, include, url
from django.conf import settings
from django.conf.urls.static import static

from django.contrib import admin
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

from termometro import views
from comentario import views, urls

admin.autodiscover()


urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'termometro.views.home', name='home'),
    url(r'^$', 'comentario.views.lista_preguntas', name='preguntas'),
    url('', include('social.apps.django_app.urls', namespace='social')),

    url(r'^comentario$', 'comentario.views.comentar', name='comentar'),
    url(r'^comentario/e$', 'comentario.views.comentar_experimento', name='comentar_experimento'),

    url(r'^comentario/votar$', 'comentario.views.votar_pregunta', name='votar_pregunta'),
    
    #Facebook
    url(r'^prueba/$', 'login.views.home'),
    url(r'^login/$', 'login.views.home'),
    url(r'^logout/$', 'login.views.logout'),
    url(r'^done/$', 'login.views.done', name='done'),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    
    url(r'^media/(?P<path>.*)$','django.views.static.serve',{'document_root':settings.MEDIA_ROOT}),
    )+ static( settings.STATIC_URL, document_root=settings.STATIC_ROOT)
