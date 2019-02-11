from django.contrib import admin
from .models import *
from urllib.request import urlopen

def check_link_status(modeladmin, request, queryset):
	for qs in queryset:

		if qs.link.startswith('http') and qs.link.endswith('.m3u8'):
			try:
				url_open = urlopen(qs.link, timeout=5)
				code = url_open.getcode()
				content_type = url_open.getheader('Content-Type')
#				print(content_type)
				if content_type.startswith('video'):
#					print(qs.link)
					qs.link_status = "Broken"
				else:
					qs.link_status = "Functional"
			except:
				qs.link_status = "Broken"
		else:
			qs.link_status = "Misspelled"

		qs.save(update_fields=['link_status'])
		

check_link_status.short_description = "Check link status"

class ChannelAdmin(admin.ModelAdmin):
	prepopulated_fields = {'slug': ('name',)}
	list_display = ['name', 'category', 'link_status']
	list_filter = ['category', 'link_status']
	search_fields = ['name']
	actions = [check_link_status]
	list_per_page=30

admin.site.register(Channel, ChannelAdmin)
admin.site.register(Category)