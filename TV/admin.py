from django.contrib import admin
from .models import *

class ChannelAdmin(admin.ModelAdmin):
	prepopulated_fields = {'slug': ('name',)}

admin.site.register(Channel, ChannelAdmin)
admin.site.register(Category)