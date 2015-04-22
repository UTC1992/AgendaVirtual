#from django.shortcuts import render
from django.views.generic import CreateView, TemplateView, ListView
from .models import Autor2
from django.core.urlresolvers import reverse_lazy

# Create your views here.
class RegistrarAutor(CreateView):
	template_name = 'autores2/registrarAutor.html'
	model = Autor2
	success_url = reverse_lazy('reportar_autor')

#class ReportarAutor(TemplateView):
#	template_name = 'autores2/reportarAutor.html'

class ReportarAutor(ListView):	
	template_name = 'autores2/reportarAutor.html'
	model = Autor2
	context_object_name = 'autores2' #es la variable k va en el for al imprimir la lista de autores2		
