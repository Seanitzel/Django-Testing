from django.http import HttpResponse
from django.shortcuts import render
from django.views import View

class HomeView(View):
	def get(self, request, *args, **kwargs):
		context = {}
		return render(request, "home.html", context)

	def post(self, request, *args, **kwargs):
		pass

	def put(self, request, *args, **kwargs):
		pass

class AboutView(View):
	def get(self, request, *args, **kwargs):
		return render(request, "about.html")

class ContactView(View):
	def get(self, request, *args, **kwargs):
		return render(request, "contact.html")

