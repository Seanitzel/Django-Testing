from django.http import HttpResponse
from django.shortcuts import render,get_object_or_404
from django.views import View
from django.db.models import Q
from django.views.generic import TemplateView,ListView,DetailView

from .models import Weight
from .form import WeightCreateForm
import random

def Weight_createview(request):
	if request.method == "POST":
		print(request.POST)
		name = request.POST.get("Name")
		weight = request.POST.get("Weight")
		obj = Weight.objects.create(
			name = name,
			weight = weight
			)
	template_name = 'website1/form.html'
	context = {}
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