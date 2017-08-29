from django.http import HttpResponse
from django.shortcuts import render
from django.views import View
from django.views.generic import TemplateView,ListView

from .models import Weight
import random

def Weights(request):
	template_name = 'weight_list.html'
	queryset = Weight.objects.all()
	context = {
	"object_list": queryset
	}
	return render(request, template_name, context)

class SeanWeightListView(ListView):
	queryset = Weight.objects.filter(name__iexact = 'sean')
	template_name = 'weight_list.html'
