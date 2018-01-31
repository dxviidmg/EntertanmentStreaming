from django.shortcuts import render, redirect
from django.views.generic import View

class ViewMain(View):
	def get(self, request):
		if request.user.is_authenticated == True:
			return redirect('accounts:Home')
		else:
			template_name = 'main/main.html'
			return render(request, template_name)