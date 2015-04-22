from django.shortcuts import render_to_response
from django.views.generic import TemplateView, FormView
from .forms import UserForm
from django.core.urlresolvers import reverse_lazy

class Registrarce(FormView):
	template_name = 'inicio/registrarce.html'
	form_class = UserForm
	success_url = reverse_lazy('registrarce')

	def form_valid(self, form):
		user = form.save()
		return super(Registrarce, self).form_valid(form)