from django.http import HttpResponse,HttpResponseRedirect
from django.shortcuts import render,get_object_or_404
from django.views import View
from django.db.models import Q
from django.views.generic import TemplateView,ListView,DetailView

from .models import Weight
from .form import WeightCreateForm
import random

def Weight_createview(request):
	form = WeightCreateForm(request.POST or None)
	errors = None
	if form.is_valid():
		obj = Weight.objects.create(
			name = form.cleaned_data.get('name'),
			weight = form.cleaned_data.get('weight')
			)
		return HttpResponseRedirect("/weight/")

	if form.errors:
		errors = form.errors

	template_name = 'website1/form.html'
	context = {"form": form, "errors": errors}
	return render(request, template_name, context)

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