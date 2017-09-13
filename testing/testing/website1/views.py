from django.http import HttpResponse,HttpResponseRedirect
from django.shortcuts import render,get_object_or_404
from django.views import View
from django.db.models import Q
from django.views.generic import TemplateView,ListView,DetailView, CreateView

from .models import Weight
from .form import WeightCreateForm,WeightForm
import random

def Weights(request):
	template_name = 'weight_list.html'
	queryset = Weight.objects.all()
	context = {
	"object_list": queryset
	}
	return render(request, template_name, context)

class WeightListView(ListView):
	template_name = 'weight_list.html'
	def get_queryset(self):
		slug = self.kwargs.get("slug")
		if slug:
			queryset = Weight.objects.filter(
				Q(name__iexact = slug) |
				Q(name__icontains = slug)
			)
		else:
			queryset = Weight.objects.all()
		return queryset

class WeightDetailView(DetailView):
	queryset = Weight.objects.all()

class WeightCreateView(CreateView):
	form_class = WeightForm
	template_name = 'website1/form.html'
	success_url = "/weight/"

	def form_valid(self, form):
		instance = form.save(commit = False)
		instance.Owner = self.request.user
		return super(WeightCreateView, self).form_valid(form)