from django.contrib import admin
from personal.models import Entry

# Register your models here.

class EntryAdmin(admin.ModelAdmin):
	fieldsets = [
		(None, {'fields': ['title']}),
		('Position', {'fields': ['position']}),
		('Category', {'fields': ['category']}),
		('Body', {'fields': ['body']}),
		('Date information', {'fields': ['start_date', 'end_date' ]}),
		('Image', {'fields': ['entry_image']}),
	]

	list_display = ('title', 'body', 'start_date')
	list_filter = ['start_date']

admin.site.register(Entry, EntryAdmin)
