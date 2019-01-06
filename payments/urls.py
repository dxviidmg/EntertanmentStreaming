from django.conf.urls import url
from . import views

app_name = 'payments'

urlpatterns = [
	url('history/(?P<username>[-\w]+)/$', views.PaymentsListView.as_view(), name="PaymentsListClient"),
	url('history/$', views.PaymentsListView.as_view(), name="PaymentsList"),
]