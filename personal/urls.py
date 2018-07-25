from django.conf.urls import url
from django.urls import path
from . import views
from django.contrib.staticfiles.urls import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf import settings

urlpatterns = [
	path('contact/', views.ContactView.as_view(), name='contact'),
	path('education/', views.EducationView.as_view(), name='education'),
	path('experience/', views.ExperienceView.as_view(), name='experience'),
	path('projects/', views.ProjectView.as_view(), name='projects'),
	path('', views.HomeView.as_view(), name='index'),
	]
