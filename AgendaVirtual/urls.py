from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.conf import settings

urlpatterns = patterns('',

	#para ver las imagenes
	url(r'^media/(?P<path>.*)$','django.views.static.serve', {'document_root': settings.MEDIA_ROOT,}),
    #ADMINISTRADOR
    url(r'^admin/', include(admin.site.urls)),
    #INICIO
    url(r'^', include('apps.inicio.urls')),
    #AUTOR
    url(r'^autor/', include('apps.autores2.urls')),
    #LIBRO
    url(r'^libros/', include('apps.libros.urls')),
)
