from django import forms
from django.contrib.auth.models import User
from .models import Profile
from django.forms.utils import ErrorList
from django.utils.translation import ugettext_lazy as _

class UserCreateForm(forms.ModelForm):
	def __init__(self, *args, **kwargs):
		super(UserCreateForm, self).__init__(*args, **kwargs)
		self.fields['first_name'].required = True
		self.fields['last_name'].required = True
		self.fields['email'].required = True

	class Meta:
		model = User
		fields = ('first_name', 'last_name', 'email', )

	def clean_email(self):
		cleaned_data = super(UserCreateForm, self).clean()
		email = cleaned_data.get("email")
		try:
			user = User.objects.exclude(pk=self.instance.pk).get(email=email)
#			print("souy e2", original_email)
		except User.DoesNotExist:
			return email
		raise forms.ValidationError(u'The email "%s" already registered.' % email)

#	def clean_email2(self):
#		email11 = self.cleaned_data['email']
#		e2 = self.cleaned_data.get('email2')
#		if email11 != e2:
#			raise forms.ValidationError('The email addresses do not match.')

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