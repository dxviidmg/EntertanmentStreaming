from django.shortcuts import render, redirect
from django.views.generic import View
from .models import *
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth import update_session_auth_hash
from django.contrib import messages
from .forms import *
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
#from django.contrib.auth.models import User
#from django.contrib.sessions.models import Session

class ViewProfile(View):
	@method_decorator(login_required)
	def get(self, request):
		template_name = "accounts/Profile.html"
		profile = Profile.objects.get(user=request.user)
		UserForm = UserUpdateForm(instance=request.user)
		ProfileForm = ProfileUpdateForm(instance=profile)
		context = {
			'profile': profile,
			'UserForm': UserForm,
			'ProfileForm': ProfileForm,
		}
		return render(request,template_name, context)
	def post(self, request):
		template_name = "accounts/Profile.html"
		profile = Profile.objects.get(user=request.user)
		UserForm = UserUpdateForm(instance=request.user, data=request.POST)
		ProfileForm = ProfileUpdateForm(instance=profile, data=request.POST, files=request.FILES)

		if UserForm.is_valid: # or ProfileForm.is_valid:
			UserForm.save()
		if ProfileForm.is_valid:
			ProfileForm.save()
			messages.success(request, 'Your profile was successfully updated!')
		return redirect('accounts:Profile')

def change_password(request):
	if request.method == 'POST':
		form = PasswordChangeForm(request.user, request.POST)
		if form.is_valid():
			user = form.save()
			update_session_auth_hash(request, user)  # Important!
			messages.success(request, 'Your password was successfully updated!')
			return redirect('accounts:change_password')
		else:
		    messages.error(request, 'Please correct the error below.')
	else:
		form = PasswordChangeForm(request.user)
	return render(request, 'accounts/change_password.html', {'form': form})

class ViewHome(View):
	def get(self, request):
		template_name = 'accounts/home.html'
		profile = Profile.objects.get(user=request.user)
		profile.UpdateLocking()

		return render(request, template_name)

class CreateViewAccount(View):
	def get(self, request):
		template_name = "accounts/create_account.html"
		UserForm = UserCreateForm()
		ProfileForm = ProfileCreateForm()
		last_account = User.objects.last()
		context = {
		'UserForm':UserForm,
		'ProfileForm': ProfileForm
		}
		return render(request,template_name,context)
	def post(self,request):
		template_name = "accounts/create_account.html"
		last_account = User.objects.last()

		UserForm = UserCreateForm(request.POST)
		ProfileForm = ProfileCreateForm(request.POST, request.FILES)
		if UserForm.is_valid() and ProfileForm.is_valid():
			NewUser = UserForm.save(commit=False)
			NewUser.username = str(last_account.pk + 1)
			NewUser.first_name = str(UserForm.cleaned_data['first_name'])
			NewUser.last_name = str(UserForm.cleaned_data['last_name'])
			NewUser.set_password('timesee1')
			NewUser.save()

			NewProfile = ProfileForm.save(commit=False)
			NewProfile.user = NewUser
			NewProfile.save()
			return redirect('payments:PaymentsListClient', NewUser.username)
#		else:
#			context = {
#			'UserForm': UserForm,
#			'ProfileForm': ProfileForm
#			}
#			return render(request,template_name,context)

class ListViewAccounts(View):
	def get(self, request):
		template_name = "accounts/list_accounts.html"
		users = User.objects.filter(is_staff=False)

		context = {
			'users': users
		}
		return render(request,template_name,context)			