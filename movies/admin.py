from django.contrib import admin
from .models import *

class MovieAdmin(admin.ModelAdmin):
	prepopulated_fields = {'slug': ('name', 'year')}
	list_display = ['name', 'category']
	list_filter = ['category', 'year']
	search_fields = ['name']

admin.site.register(Movie, MovieAdmin)
admin.site.register(Category)