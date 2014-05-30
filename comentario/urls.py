from django.conf.urls import patterns, include, url

from comentario import views

urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'comentario.views.comentar', name='comentar'),
    # url(r'^blog/', include('blog.urls')),

)
