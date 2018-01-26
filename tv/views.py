from django.shortcuts import render, get_object_or_404
from django.views.generic import View
from .models import *
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator

class ChannelsListView(View):
	@method_decorator(login_required)
	def get(self, request):
		template_name = 'TV/ChannelsList.html'
		categories = Category.objects.all()

		ListOfChannelsByCategory = []

		for category in categories:
			ListOfChannelsByCategory.append({'category': category.name, 'channels': Channel.objects.filter(category=category)})

		context = {
			'ListOfChannelsByCategory': ListOfChannelsByCategory,
		}
		return render(request, template_name, context)

class ChannelDetailView(View):
	@method_decorator(login_required)
	def get(self, request, slug):
		template_name = 'TV/ChannelDetail.html'
		channel = get_object_or_404(Channel, slug=slug)
		category = Category.objects.get(pk=channel.category.pk)
		similarChannels = Channel.objects.filter(category=category).exclude(pk=channel.pk)
		context = {
			'channel': channel,
			'category': category,
			'similarChannels': similarChannels,
		}
		return render(request, template_name, context)