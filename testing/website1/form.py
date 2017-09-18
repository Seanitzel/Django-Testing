from django import forms
from .models import Person
import datetime

class PersonCreateForm(forms.Form):
	name = forms.CharField()
	workout = forms.CharField()
	starting_weight = forms.FloatField()
	date = forms.DateField(initial=datetime.date.today)

class PersonForm(forms.ModelForm):
	class Meta:
		model = Person
		fields = [
		'name',
		'starting_weight',
		'workout',
		]