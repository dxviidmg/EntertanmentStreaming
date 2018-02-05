from django import forms
from django.contrib.auth.models import User
from .models import Profile

class UserCreateForm(forms.ModelForm):	
	class Meta:
		model = User
		fields = ('first_name', 'last_name', 'email')

#	def clean_password2(self):
#		cd = self.cleaned_data
#		if cd['password'] != cd['password2']:
#			raise forms.ValidationError('Los passwords no coicinden')
#		return cd['password2']

#	def clean_username(self):
#		cd = self.cleaned_data['username']
#		if User.objects.filter(username=cd).exists():
#			raise forms.ValidationError("Este usuario ya ha sido registrado")
#		return cd

	def clean_email(self):
		cd = self.cleaned_data['email']
		if User.objects.filter(email=cd).exists():
			raise forms.ValidationError("This email has already been registered")
		return cd

class ProfileCreateForm(forms.ModelForm):
	class Meta:
		model = Profile
		fields = ('phone', 'is_internet_client')

class UserUpdateForm(forms.ModelForm):
	
	class Meta:
		model = User
		fields = ('first_name', 'last_name',)

class ProfileUpdateForm(forms.ModelForm):
	class Meta:
		model = Profile
		fields = ('photo', 'phone')		