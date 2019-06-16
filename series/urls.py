from django.conf.urls import url
from . import views

app_name = 'Series'

urlpatterns = [
	url('chapter/(?P<slug>[-\w]+)/$', views.ChapterDetailView.as_view(), name="ChapterDetail"),
	url('serie/(?P<slug>[-\w]+)/$', views.SerieDetailView.as_view(), name="SerieDetail"),
	url('series/$', views.SeriesListView.as_view(), name="SeriesList"),
]