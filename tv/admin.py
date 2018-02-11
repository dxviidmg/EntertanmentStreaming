from django.contrib import admin
from .models import *

class ChannelAdmin(admin.ModelAdmin):
	prepopulated_fields = {'slug': ('name',)}
	list_display = ['name', 'category']
	list_filter = ['category']
	search_fields = ['name']

admin.site.register(Channel, ChannelAdmin)
admin.site.register(Category)