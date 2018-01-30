from django.contrib import admin
from .models import *
from django.contrib.auth.models import User

admin.site.register(Profile)

class UserAdmin(admin.ModelAdmin):
	search_fields = ['email']
	list_display = ['first_name', 'last_name', 'email', 'is_active']
#	actions = [ExportUsersCSV("export_csv")]
	#prepopulated_fields = {'first_name': ('username')}

admin.site.unregister(User)
admin.site.register(User, UserAdmin)

#admin.site.register(User)