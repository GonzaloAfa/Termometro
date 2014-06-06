from django.conf.urls import patterns, include, url
from django.contrib import admin
from termometro import views
from comentario import views, urls
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'termometro.views.home', name='home'),
    url(r'^comentario/', include('comentario.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    url('', include('social.apps.django_app.urls', namespace='social')),
    url(r'^login/$', 'login.views.prueba'),
    url(r'^login/new-association-redirect-url/$', 'login.views.response'),
    url(r'^login/new-user/$', 'login.views.response'),



    #url(r'^principal/', include('principal.urls')),

)
