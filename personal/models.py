from django.db import models
import os

def get_upload_path(instance, filename):
	return os.path.join(
		instance.category, instance.title, filename)

# Categories for organizing and populating views
CATEGORIES = (
	('Education', 'Education'),
	('Work Experience', 'Work Experience'),
	('Projects', 'Projects'),
)

# Categories for populating welcome and contact pages
BASIC_CATEGORIES = (
	('Contact', 'Contact'),
    ('Home', 'Home'),
)

# For education, projects, and work experience
class Entry(models.Model):
	title = models.CharField(max_length=140)
	position = models.CharField(max_length=140, blank=True)
	location = models.CharField(max_length=140, blank=True)
	category = models.CharField(max_length=140, choices=CATEGORIES)
	body = models.TextField()
	start_date = models.DateTimeField('start date')
	end_date = models.DateTimeField('end date')
	entry_image = models.ImageField(upload_to=get_upload_path, blank = True, null=True)

	def __str__(self):
		return self.title

# For welcome and contact pages
class Basic(models.Model):
	title = models.CharField(max_length=30)
	category = models.CharField(max_length=140, choices=BASIC_CATEGORIES)
	body = models.TextField()

	def __str__(self):
		return self.title 
