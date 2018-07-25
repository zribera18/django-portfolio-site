from django.contrib import admin
from personal.models import Entry, Basic

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

class BasicAdmin(admin.ModelAdmin):
	fieldsets = [
		('Title', {'fields': ['title']}),
		('Category', {'fields': ['category']}),
		('Body', {'fields': ['body']}),
	]
	list_display = ('title', 'category')

admin.site.register(Entry, EntryAdmin)
admin.site.register(Basic, BasicAdmin)
