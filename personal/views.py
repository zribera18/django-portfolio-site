from django.shortcuts import render
from django.http import HttpResponse
from django.views import generic
from .models import Entry, Basic

# display image and summary of Education experience
class EducationView(generic.ListView):
	model = Entry
	template_name = 'personal/resume.html'
	context_object_name = 'entry_list'
	def get_queryset(self):
		return Entry.objects.filter(category = 'Education').order_by('-start_date')

# display image and summary of Career Experience
class ExperienceView(generic.ListView):
	model = Entry
	template_name = 'personal/resume.html'
	context_object_name = 'entry_list'
	def get_queryset(self):
		return Entry.objects.filter(category = 'Work Experience').order_by('-start_date')

# display images and summary of personal projects
class ProjectView(generic.ListView):
	model = Entry
	template_name = 'personal/projects.html'
	context_object_name = 'entry_list'
	def get_queryset(self):
		return Entry.objects.filter(category = 'Projects').order_by('-start_date')

# a place to introduce yourself
# in admin view, you can input html to further style this section
class HomeView(generic.ListView):
	model = Basic
	template_name = 'personal/basic.html'
	context_object_name = 'entry_list'
	def get_queryset(self):
		return Basic.objects.filter(category = 'Home')

# contact Information
class ContactView(generic.ListView):
	model = Basic
	template_name = 'personal/basic.html'
	context_object_name = 'entry_list'
	def get_queryset(self):
		return Basic.objects.filter(category = 'Contact')
