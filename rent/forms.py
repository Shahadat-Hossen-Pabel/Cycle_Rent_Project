from django import forms


class FinalForm(forms.Form):
	pickup_date = forms.DateField(widget=forms.TextInput(attrs={
		'class' : 'form-control',
		'type': 'date'
	}))
	pickup_time = forms.TimeField(widget=forms.TextInput(attrs={
		'class' : 'form-control',
		'type': 'time'
	}))
	pickout_date = forms.DateField(widget=forms.TextInput(attrs={
		'class' : 'form-control',
		'type': 'date'
	}))
	pickout_time = forms.TimeField(widget=forms.TextInput(attrs={
		'class' : 'form-control',
		'type': 'time'
	}))