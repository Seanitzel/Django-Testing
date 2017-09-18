from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponse,HttpResponseRedirect
from django.shortcuts import render,get_object_or_404
from django.views import View
from django.db.models import Q
from django.views.generic import TemplateView,ListView,DetailView, CreateView

from .models import Person
from .form import PersonCreateForm,PersonForm
import random

class PersonListView(LoginRequiredMixin, ListView):
	template_name = 'people_list.html'
	def get_queryset(self):
		return Person.objects.filter(Owner = self.request.user)

class PersonDetailView(LoginRequiredMixin, DetailView):
	queryset = Person.objects.all()

class PersonCreateView(LoginRequiredMixin, CreateView):
	form_class = PersonForm
	template_name = 'website1/form.html'

	def form_valid(self, form):
		instance = form.save(commit = False)
		instance.Owner = self.request.user
		return super(PersonCreateView, self).form_valid(form)