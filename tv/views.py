from django.shortcuts import render, get_object_or_404
from django.views.generic import View
from .models import *
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
import random
import urllib.request

class ChannelsListView(View):
	@method_decorator(login_required)
	def get(self, request):
		template_name = 'TV/list_channels.html'
		categories = Category.objects.all()

		ListOfChannelsByCategory = []

		for category in categories:
			ListOfChannelsByCategory.append({'category': category.name, 'channels': Channel.objects.filter(category=category)})

		string = ""
		data = urllib.request.urlopen('http://tecnotv.xyz/lista.m3u')
		
		for line in data:
			line = line.decode("utf-8").replace('\n', ' ').replace('\n', '  ').replace('\n', '   ') 
			string = string + line
		data.close()

		con = 0
		channels = []

		for sentence_channel in string.split('#EXTINF:-1 '):
			data_channel = sentence_channel.split()
			if data_channel[0].startswith('tvg-logo') and data_movie[-1].endswith('m3u8'):
				logo = data_channel[0][10:-1]
				link = data_channel[-1]

				try:
					urllib.request.urlopen(link, timeout=1)
					urllib.request.urlopen(logo, timeout=1)
#					con = con + 1
#					print(con, link)
#					channels.append('pago':PagoRenta.objects.all())

				except:
					pass					

		print(channels)
		context = {
			'ListOfChannelsByCategory': ListOfChannelsByCategory,
		}
		return render(request, template_name, context)

class ChannelDetailView(View):
	@method_decorator(login_required)
	def get(self, request, slug):
		template_name = 'TV/detail_channel.html'
		channel = get_object_or_404(Channel, slug=slug)
		category = Category.objects.get(pk=channel.category.pk)
		similarChannels = Channel.objects.filter(category=category).exclude(pk=channel.pk)
		listChannels = list(similarChannels)

		if len(listChannels) < 6:
			randomChannels = random.sample(listChannels, len(listChannels))
		else:
			randomChannels = random.sample(listChannels, 6)

		context = {
			'channel': channel,
			'category': category,
			'randomChannels': randomChannels,
		}
		return render(request, template_name, context)