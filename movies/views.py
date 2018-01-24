from django.shortcuts import render, get_object_or_404
from django.views.generic import View
from .models import *
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator

class MoviesListView(View):
#	@method_decorator(login_required)
	def get(self, request):
		template_name = 'movies/MoviesList.html'
		categories = Category.objects.all()

		ListOfMoviesByCategory = []

		for category in categories:
			ListOfMoviesByCategory.append({'category': category.name, 'movies': Movie.objects.filter(category=category)})

		context = {
			'ListOfMoviesByCategory': ListOfMoviesByCategory,
		}
		return render(request, template_name, context)

class MovieDetailView(View):
#	@method_decorator(login_required)
	def get(self, request, slug):
		template_name = 'movies/MovieDetail.html'
		movie = get_object_or_404(Movie, slug=slug)
		category = Category.objects.get(pk=movie.category.pk)
		similarMovies = Movie.objects.filter(category=category).exclude(pk=movie.pk)
		context = {
			'movie': movie,
			'category': category,
			'similarMovies': similarMovies,
		}
		return render(request, template_name, context)