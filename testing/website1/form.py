from django import forms

class WeightCreateForm(forms.Form):
	name = forms.CharField()
	weight = forms.FloatField()

	def clean_name(self):
		name = self.cleaned_data.get("name")
		if name == "hola":
			raise forms.ValidationError("NOT A NAME!")
		return name