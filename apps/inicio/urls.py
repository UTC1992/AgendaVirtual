from django.conf.urls import patterns, include, url
from .views import Registrarce
#from .views import index2

urlpatterns = patterns('',
	url(r'^$', 'django.contrib.auth.views.login', 
		{'template_name':'inicio/index.html'}, name = 'login'),
	url(r'^cerrar/$', 'django.contrib.auth.views.logout_then_login', 
		name = 'logout'),
	url(r'^registrarce/$', Registrarce.as_view(),
		name = 'registrarce'),
)
