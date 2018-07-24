from django.contrib import admin
from personal.models import Entry, Home

# Register your models here.

class EntryAdmin(admin.ModelAdmin):
	fieldsets = [
		(None, {'fields': ['title']}),
		('Position', {'fields': ['position']}),
		('Location', {'fields': ['location']}),
		('Category', {'fields': ['category']}),
		('Body', {'fields': ['body']}),
		('Date information', {'fields': ['start_date', 'end_date' ]}),
		('Image', {'fields': ['entry_image']}),
	]

	list_display = ('title', 'category', 'location', 'position', 'start_date')
	list_filter = ['start_date']

class HomeAdmin(admin.ModelAdmin):
	fieldsets = [
		('Title', {'fields': ['title']}),
		('Body', {'fields': ['body']}),
	]

admin.site.register(Entry, EntryAdmin)

admin.site.register(Home, HomeAdmin)
