from django.shortcuts import render
from django.views.generic import View
from django.contrib.auth.models import User
from .models import *
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator

class PaymentsListView(View):
	@method_decorator(login_required)
	def get(self, request):
		template_name = 'payments/PaymentsList.html'
		user = User.objects.get(pk=request.user.pk)
		payments = Payment.objects.filter(user=user)

		context = {
			'payments': payments,
		}
		return render(request, template_name, context)