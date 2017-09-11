from django import forms

class WeightCreateForm(forms.Form):
	name = forms.CharField(required = False)
	weight = forms.FloatField(required = False)