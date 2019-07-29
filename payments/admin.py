from django.contrib import admin
from .models import *

class PaymentAdmin(admin.ModelAdmin):
	date_hierarchy = 'created'	
#	prepopulated_fields = {'slug': ('season__number')}
	list_display = ['user', 'created', 'quantity', 'author']
	list_filter = ['created']
#	search_fields = ['name']
#	list_per_page=40

admin.site.register(Payment, PaymentAdmin)