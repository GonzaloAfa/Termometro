from django.conf.urls import patterns, include, url

from django.conf import settings
from django.conf.urls.static import static

from comentario import views

urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'comentario.views.comentar', name='comentar'),
    # url(r'^blog/', include('blog.urls')),

)#+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
