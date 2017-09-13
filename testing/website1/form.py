from django import forms
from .models import Weight

class WeightCreateForm(forms.Form):
	name = forms.CharField()
	workout = forms.CharField()
	weight = forms.FloatField()

class WeightForm(forms.ModelForm):
	class Meta:
		model = Weight
		fields = [
		'name',
		'weight',
		'workout'
		]