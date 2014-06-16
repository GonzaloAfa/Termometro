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
    url(r'^$', 'termometro.views.home', name='home'),
    url('', include('social.apps.django_app.urls', namespace='social')),
    
    url(r'^comentario/', include('comentario.urls')),
    url(r'^preguntas/', 'comentario.views.lista_preguntas', name='preguntas'),    
    
    url(r'^prueba/$', 'login.views.home'),

    #Facebook
    url(r'^login/$', 'login.views.home'),
    url(r'^logout/$', 'login.views.logout'),
    url(r'^done/$', 'login.views.done', name='done'),


    url(r'^admin/', include(admin.site.urls)),
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    
    url(r'^media/(?P<path>.*)$','django.views.static.serve',{'document_root':settings.MEDIA_ROOT}),
    )+ static( settings.STATIC_URL, document_root=settings.STATIC_ROOT)
