from django.conf.urls import url
from . import views

app_name = 'TV'

urlpatterns = [
	url('channel/(?P<slug>[-\w]+)/$', views.ChannelDetailView.as_view(), name="ChannelDetail"),
	url('channels', views.ChannelsListView.as_view(), name="ChannelsList"),
]