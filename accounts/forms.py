from django import forms
from django.contrib.auth.models import User
from .models import Profile

class UserCreateForm(forms.ModelForm):	
	class Meta:
		model = User
		fields = ('first_name', 'last_name', 'email')

class ProfileCreateForm(forms.ModelForm):
	class Meta:
		model = Profile
		fields = ('country', 'phone', 'is_internet_client')

class UserUpdateForm(forms.ModelForm):	
	class Meta:
		model = User
		fields = ('first_name', 'last_name',)

class ProfileUpdateForm(forms.ModelForm):
	class Meta:
		model = Profile
		fields = ('photo', 'phone')