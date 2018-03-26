from django.contrib import admin
from .models import *
import urllib.request 

def check_link_status(modeladmin, request, queryset):
	for qs in queryset:
		try:
			urllib.request.urlopen(qs.link, timeout=1)
			qs.link_status = "Functional"
			qs.save(update_fields=['link_status'])
		except:
			qs.link_status = "Broken"
			qs.save(update_fields=['link_status'])

check_link_status.short_description = "Check link status"

class ChannelAdmin(admin.ModelAdmin):
	prepopulated_fields = {'slug': ('name',)}
	list_display = ['name', 'category', 'link_status']
	list_filter = ['category', 'link_status']
	search_fields = ['name']
	actions = [check_link_status]

admin.site.register(Channel, ChannelAdmin)
admin.site.register(Category)