from django.shortcuts import render, get_object_or_404
from django.views.generic import View
from .models import *
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.db.models import Q
import operator
from functools import reduce
import random

class MoviesListView(View):
	@method_decorator(login_required)
	def get(self, request):
		template_name = 'movies/list_movies.html'
		categories = Category.objects.all()

		query = request.GET.get("query")

		ListOfMoviesByCategory = []

		for category in categories:
			if query:
				ListOfMoviesByCategory.append({'category': category.name, 'movies': Movie.objects.filter(category=category, link_status="Functional", name__contains=query)})
			else:
				ListOfMoviesByCategory.append({'category': category.name, 'movies': Movie.objects.filter(category=category, link_status="Functional")})

		context = {
			'ListOfMoviesByCategory': ListOfMoviesByCategory,
		}
		return render(request, template_name, context)

class MovieDetailView(View):
	@method_decorator(login_required)
	def get(self, request, slug):
		template_name = 'movies/detail_movie.html'
		movie = get_object_or_404(Movie, slug=slug)
		name_movie = movie.name.split()
		category = Category.objects.get(pk=movie.category.pk)
		similarMovies = Movie.objects.filter(category=category).exclude(pk=movie.pk)

		condition1 = reduce(operator.or_,[Q(name__icontains=work) for work in name_movie])
		similarMovies = similarMovies.filter(Q(condition1) | Q(year=movie.year))

		listMovies = list(similarMovies)

		if len(listMovies) < 6:
			randomMovies = random.sample(listMovies, len(listMovies))
		else:
			randomMovies = random.sample(listMovies, 6)

		context = {
			'movie': movie,
			'category': category,
			'randomMovies': randomMovies,
		}
		return render(request, template_name, context)