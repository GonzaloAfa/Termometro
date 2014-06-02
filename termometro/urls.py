from django.conf.urls import patterns, include, url

from django.conf import settings
from django.conf.urls.static import static

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
    #url(r'^principal/', include('principal.urls')),

)+ static( settings.STATIC_URL, document_root=settings.STATIC_ROOT)
