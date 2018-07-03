from django.shortcuts import render
from django.http import HttpResponse
from django.views import generic
from .models import Entry
# Create your views here.

class EducationView(generic.ListView):
	model = Entry
	template_name = 'personal/resume.html'
	context_object_name = 'entry_list'

	def get_queryset(self):
		return Entry.objects.filter(category = 'Education').order_by('-start_date')
	
class ExperienceView(generic.ListView):
	model = Entry
	template_name = 'personal/resume.html'
	context_object_name = 'entry_list'
	def get_queryset(self):
		return Entry.objects.filter(category = 'Work Experience').order_by('-start_date')

def index(request):
	return render(request, 'personal/home.html')

def contact(request):
	return render(request, 'personal/basic.html', {'content':['If you would like to get in touch, please email me at:', 'zribera18@gmail.com', 'Or by phone at:', '(510)846-7086']})

#def education(request):
#	template_name = 'personal/resume.html'
#	context_object_name = 'education_entry_list'
	
#	def get_queryset(self):
#		return render(request, Entry.objects.filter(category='Education'))
#	return render(request, 'personal/resume.html',  {'content':Entry.objects.filter(category='Education')})

def experience(request):
	return render(request, 'personal/basic.html', {'content':['Work Experience']})
