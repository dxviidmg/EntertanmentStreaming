from django.contrib import admin
from .models import *

admin.site.register(Category)
admin.site.register(Season)
admin.site.register(Chapter)

class SerieAdmin(admin.ModelAdmin):
	prepopulated_fields = {'slug': ('name', 'year')}
#	list_display = ['name', 'category', 'link_status']
#	list_filter = ['category', 'year']
#	search_fields = ['name']
#	actions = [check_link_status]
#	list_per_page=30

admin.site.register(Serie, SerieAdmin)