from django.conf.urls import patterns, include, url

from django.contrib import admin
from termometro import views
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'termometro.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    #url(r'^principal/', include('principal.urls')),

)
