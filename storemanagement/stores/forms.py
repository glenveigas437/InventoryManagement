from django import forms
from .models import *

class ProductForm(forms.ModelForm):
	class Meta:
		model = Product
		fields = ('prod_name', 'company', 'quantity', 'price', 'units', 'prod_type')

class UpdateProduct(forms.ModelForm):
	class Meta:
		model = Product
		fields = ('units',)



