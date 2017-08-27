from django.http import HttpResponse
from django.shortcuts import render
from django.views import View
from django.views.generic import TemplateView

import random

class HomeView(TemplateView):
	template_name = 'home.html'

	def get_context_data(self, *args, **kwargs):
		context = super(HomeView, self).get_context_data(*args, **kwargs)
		num = None
		num_list = [random.randint(0,1000000),
					random.randint(0,1000000),
					random.randint(0,1000000)]
		context = {	"num": num,
					"num_list": num_list
					}
		print(context)
		return context

