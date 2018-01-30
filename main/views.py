from django.shortcuts import render
from django.views.generic import View

class ViewMain(View):
	def get(self, request):
		template_name = 'main/main.html'
		return render(request, template_name)