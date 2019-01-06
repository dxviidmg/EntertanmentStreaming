from django.shortcuts import render, redirect
from django.views.generic import View
from django.contrib.auth.models import User
from .models import *
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from .forms import *

class PaymentsListView(View):
	@method_decorator(login_required)
	def get(self, request, pk=None):
		template_name = 'payments/list_payments.html'
		if request.user.is_staff:
			user = User.objects.get(pk=pk)
		else:
			user = User.objects.get(pk=request.user.pk)

		user.profile.update_status()		
		form = PaymentCreateForm(user=user, author=request.user)
		payments = Payment.objects.filter(user=user)

		context = {
			'user': user,
			'payments': payments,
			'form': form,
		}
		return render(request, template_name, context)
	def post(self, request, pk=None):
		template_name = 'payments/PaymentsList.html'		
		if request.user.is_staff:
			user = User.objects.get(pk=pk)
		else:
			user = User.objects.get(pk=request.user.pk)
		
		form = PaymentCreateForm(data=request.POST, files=request.FILES, author=request.user, user=user)
		if form.is_valid():
			form.save()		
		return redirect('payments:PaymentsListClient', user.pk)