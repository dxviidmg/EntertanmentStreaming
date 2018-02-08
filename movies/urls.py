from django.conf.urls import url
from . import views

app_name = 'Movies'

urlpatterns = [
	url('movie/(?P<slug>[-\w]+)/$', views.MovieDetailView.as_view(), name="MovieDetail"),
	url('movies/$', views.MoviesListView.as_view(), name="MoviesList"),
]