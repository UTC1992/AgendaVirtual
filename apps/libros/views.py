from django.shortcuts import render
from django.views.generic import TemplateView
from .models import Libro
from apps.autores2.models import Autor2

# Create your views here.
class BuscarView(TemplateView):
	template_name = 'libros/buscar.html'

	def post(self, request, *args, **kwargs):
		buscar = request.POST['datoBuscado']
		libros = Libro.objects.filter(nombre__contains = buscar)
		print libros
		if libros:
			#print "Ha preguntado por un libro"
			datos = []
			for libro in libros:
				autores = libro.autor.all()
				datos.append(dict([(libro,autores)]))
			#print datos
			return render(request,'libros/buscar.html',
				{'datos':datos})

		else:
			autores = Autor2.objects.filter(nombre__contains = buscar)
			#print autores
		return render(request, 'libros/buscar.html',
			{'autores':autores, 'autor':True})