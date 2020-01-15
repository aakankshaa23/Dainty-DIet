from django import forms
from .models import RestaurantLocation
from .validators import validate_category

class RestaurantForm(forms.Form):
	name= forms.CharField()
	location=forms.CharField(required=False)
	category=forms.CharField(required=False)

	def clean_name(self):
		name=self.cleaned_data.get("name")
		if name=='hello':
			raise forms.ValidationError("not a valid name")
		return name

class ModelCreateForm(forms.ModelForm):
	#category = forms.CharField(required=False,validators=[validate_category])
	class Meta:
		model=RestaurantLocation
		fields=[
		'name',
		'location',
		'category',
				]
	def clean_name(self):
		name=self.cleaned_data.get("name")
		if name=='hello':
			raise forms.ValidationError("not a valid name")
		return name