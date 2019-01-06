from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import View
from django.contrib.auth.models import User
from .models import *
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from .forms import *

class PaymentsListView(View):
	@method_decorator(login_required)
	def get(self, request, username=None):
		template_name = 'payments/list_payments.html'
		if request.user.is_staff:
			author = get_object_or_404(User, username=request.user.username)
			user = User.objects.get(username=username)
			form = PaymentCreateForm(user=user, author=author)
		else:
			user = User.objects.get(username=request.user.username)
			form = None
			user.profile.update_status()

		payments = Payment.objects.filter(user=user)

		context = {
			'user': user,
			'payments': payments,
			'form': form,
		}
		return render(request, template_name, context)
	def post(self, request, username=None):
#		if request.user.is_staff:
		author = get_object_or_404(User, username=request.user.username)
		user = User.objects.get(username=username)
#			form = PaymentCreateForm(user=user, author=author)
		form = PaymentCreateForm(data=request.POST, files=request.FILES, author=request.user, user=user)
		if form.is_valid():
			form.save()
#		else:
#			user = User.objects.get(user=request.username)
#			form = None

		return redirect('payments:PaymentsListClient', user.username)