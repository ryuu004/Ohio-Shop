from django import forms

from .models import Sells


class UserData(forms.Form):
	fullname = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Name', 'style': 'width: 300px;' 'height: 30px;' }))
	email    = forms.EmailField(widget=forms.EmailInput(attrs={'placeholder': 'rhyiotahari@gmail.com', 'style': 'width: 300px;' 'height: 30px;' 'margin-left: 34px;' }))
	item     = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Item', 'style': 'width: 300px;' 'height: 30px;' 'margin-left: 43px;' }))
	quantity = forms.DecimalField(widget=forms.NumberInput(attrs={'style': 'width: 38px;' 'height: 30px;' 'margin-left: 4px;' }))