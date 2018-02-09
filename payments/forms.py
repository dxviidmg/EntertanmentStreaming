from django import forms
from .models import Payment

class PaymentCreateForm(forms.ModelForm):
	class Meta:
		model = Payment
		fields = ('months', 'method', 'reference_number', 'voucher',)

	def __init__(self, *args, **kwargs):
		self.user = kwargs.pop('user')
		self.author = kwargs.pop('author')	
		super(PaymentCreateForm, self).__init__(*args, **kwargs)

	def save(self, commit=True):
		instance = super(PaymentCreateForm, self).save(commit=False)
		instance.user = self.user
		instance.author = self.author
		if commit:
			instance.save()
		return instance