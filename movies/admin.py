from django.contrib import admin
from .models import *
from urllib.request import urlopen

def check_link_status(modeladmin, request, queryset):
	for qs in queryset:
		try:
			url_open = urlopen(qs.link, timeout=5)
			code = url_open.getcode()
			content_type = url_open.getheader('Content-Type')
#			print(code)
			qs.link_status = "Functional"
		except:
			qs.link_status = "Broken or Misspelled"

		qs.save(update_fields=['link_status'])
		
check_link_status.short_description = "Check link status"

class MovieAdmin(admin.ModelAdmin):
	prepopulated_fields = {'slug': ('name', 'year')}
	list_display = ['name', 'category', 'link_status']
	list_filter = ['category', 'year']
	search_fields = ['name']
	actions = [check_link_status]
	list_per_page=30

admin.site.register(Movie, MovieAdmin)
admin.site.register(Category)