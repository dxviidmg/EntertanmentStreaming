from django.conf.urls import url
from . import views
from django.contrib.auth.views import login, logout, password_reset, password_reset_done, password_reset_confirm, password_reset_complete

app_name = 'accounts'

urlpatterns = [
	#Redirects
	url(r'^login', login,name="login"),
	url(r'^logout/$', logout, name="logout"),
	#Home
	url(r'^account/profile/$', views.ViewProfile.as_view(), name="Profile"),
	url(r'^account/home/$', views.ViewHome.as_view(), name="Home"),	
	#Accounts
	url(r'^accounts/new/$', views.CreateViewAccount.as_view(), name="CreateAccount"),
	url(r'^accounts/list/$', views.ListViewAccounts.as_view(), name="ListAccounts"),
	#Change password
	url(r'^password/$', views.change_password, name='change_password'),
	#Reset password
	url(r'^reset-password/$', password_reset, {'template_name': 'accounts/reset_password.html', 'post_reset_redirect': 'accounts:password_reset_done', 'email_template_name': 'accounts/reset_password_email.html'}, name='reset_password'),
	url(r'^reset-password/done/$', password_reset_done, {'template_name': 'accounts/reset_password_done.html'}, name='password_reset_done'),
	url(r'^reset-password/confirm/(?P<uidb64>[0-9A-Za-z]+)-(?P<token>.+)/$', password_reset_confirm, {'template_name': 'accounts/reset_password_confirm.html', 'post_reset_redirect': 'accounts:password_reset_complete'}, name='password_reset_confirm'),
	url(r'^reset-password/complete/$', password_reset_complete,{'template_name': 'accounts/reset_password_complete.html'}, name='password_reset_complete'),
    ]