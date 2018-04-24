from django import forms
from django.contrib.auth.models import User
from .models import Profile
from django.forms.utils import ErrorList

class UserCreateForm(forms.ModelForm):
	email2 = forms.CharField(label='Confirm the email address',widget=forms.TextInput)	

	class Meta:
		model = User
		fields = ('first_name', 'last_name', 'email')

	def clean_email(self):
		email = self.cleaned_data['email']
		try:
			user = User.objects.exclude(pk=self.instance.pk).get(email=email)
		except User.DoesNotExist:
			return email
		raise forms.ValidationError(u'The email "%s" already registered.' % email)

	def clean_email2(self):
		cd = self.cleaned_data
		if cd['email'] != cd['email2']:
			raise forms.ValidationError('The email addresses do not match.')

	def __init__(self, *args, **kwargs):
		super(UserCreateForm, self).__init__(*args, **kwargs)
		self.fields['first_name'].required = True
		self.fields['last_name'].required = True
		self.fields['email'].required = True

class ProfileCreateForm(forms.ModelForm):
	class Meta:
		model = Profile
		fields = ('country', 'phone')

class UserUpdateForm(forms.ModelForm):	
	class Meta:
		model = User
		fields = ('first_name', 'last_name')

class ProfileUpdateForm(forms.ModelForm):
	class Meta:
		model = Profile
		fields = ('photo', 'phone')