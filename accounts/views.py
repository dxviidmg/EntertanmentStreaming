from django.shortcuts import render, redirect
from django.views.generic import View
from .models import *
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth import update_session_auth_hash
from django.contrib import messages
from .forms import *
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required

class ViewProfile(View):
	@method_decorator(login_required)
	def get(self, request):
		template_name = "accounts/viewProfile.html"
		profile = Profile.objects.get(user=request.user)
		UserForm = UserUpdateForm(instance=request.user)
		ProfileForm = ProfileCreateForm(instance=profile)
		
		context = {
			'profile': profile,
			'UserForm': UserForm,
			'ProfileForm': ProfileForm,
		}
		return render(request,template_name, context)
#	def post(self, request):
#		template_name = "accounts/viewProfile.html"
#		perfil = Perfil.objects.get(user=request.user)
#		EdicionUserForm = UserEditForm(instance=request.user, data=request.POST)
#		EdicionPerfilForm = PerfilCreateForm(instance=perfil, data=request.POST, files=request.FILES)

#		if EdicionUserForm.is_valid:
#			EdicionUserForm.save()
#		if EdicionPerfilForm.is_valid:
#			EdicionPerfilForm.save()
#		return redirect('accounts:ViewProfile')

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
	return render(request, 'accounts/change_password.html', {
		'form': form
	})

