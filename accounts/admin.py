from django.contrib import admin
from .models import *
from django.contrib.auth.models import User
from django.contrib.auth.admin import UserAdmin
from payments.models import *

class ProfileInline(admin.StackedInline):
	model = Profile
	can_delete = False
	fk_name = 'user'

class PaymentsInline(admin.StackedInline):
	model = Payment
	can_delete = False
	fk_name = 'user'	

class CustomUserAdmin(UserAdmin):
	inlines = (ProfileInline, PaymentsInline)

	def get_inline_instances(self, request, obj=None):
		if not obj:
			return list()
		return super(CustomUserAdmin, self).get_inline_instances(request, obj)

admin.site.unregister(User)
admin.site.register(User, CustomUserAdmin)

admin.site.register(Profile)
