from django import forms
from .models import Weight

class WeightCreateForm(forms.Form):
	name = forms.CharField()
	weight = forms.FloatField()

	def clean_name(self):
		name = self.cleaned_data.get("name")
		if name == "hola":
			raise forms.ValidationError("NOT A NAME!")
		return name

class WeightForm(forms.ModelForm):
	class Meta:
		model = Weight
		fields = [
		'name',
		'weight'
		]