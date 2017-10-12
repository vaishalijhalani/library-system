from django import forms

class checkoutForm(forms.Form):
	name = forms.CharField(required=True, label="NAME ON CARD")
	cardNumber = forms.CharField(required=True, label="CARD NUMBER")
	validDate = forms.DateField(required=True, label="Expiry Date")
	cvvNumber = forms.CharField(required=True, label="CVV")
	
	