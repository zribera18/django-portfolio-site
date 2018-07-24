from django.db import models
import os

# Create your models here.

def get_upload_path(instance, filename):
	return os.path.join(
		instance.category, instance.title, filename)

CATEGORIES = (
	('Education', 'Education'),
	('Work Experience', 'Work Experience'),
	('Projects', 'Projects'),
	('Ya', 'Ya'),
)

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

class Home(models.Model):
	title = models.CharField(max_length=30)
	body = models.TextField()

	def __str__(self):
		return self.title 
