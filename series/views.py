from django.shortcuts import render
from django.views.generic import View
from .models import *
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.db.models import Q
import operator
from functools import reduce
import random

class SeriesListView(View):
	@method_decorator(login_required)
	def get(self, request):
		template_name = 'series/list_series.html'
		categories = Category.objects.filter()

		request.user.profile.update_status()
		
		ListOfSeriesByCategory = []

		for category in categories:
			ListOfSeriesByCategory.append({'category': category.name, 'series': Serie.objects.filter(category=category)})

		context = {
			'ListOfSeriesByCategory': ListOfSeriesByCategory,
		}
		return render(request, template_name, context)

class SerieDetailView(View):
	@method_decorator(login_required)
	def get(self, request, slug):
		template_name = 'series/detail_serie.html'
		serie = Serie.objects.get(slug=slug)
		seasons = Season.objects.filter(serie=serie)
		request.user.profile.update_status()
		
		ListOfChaptersBySeason = []

		for season in seasons:
			ListOfChaptersBySeason.append({'season': season.number, 'chapters': Chapter.objects.filter(season=season)})

		context = {
			'serie': serie,
			'ListOfChaptersBySeason': ListOfChaptersBySeason,
		}
		return render(request, template_name, context)

class ChapterDetailView(View):
	@method_decorator(login_required)
	def get(self, request, slug):
		template_name = 'series/detail_chapter.html'
		chapter = Chapter.objects.get(slug=slug)

		context = {
			'chapter': chapter,
		}
		return render(request, template_name, context)		