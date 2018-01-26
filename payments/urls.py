from django.conf.urls import url
from . import views

app_name = 'payments'

urlpatterns = [
	url('history', views.PaymentsListView.as_view(), name="PaymentsList"),
]