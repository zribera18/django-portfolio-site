from django.conf.urls import url
from django.urls import path
from . import views
from django.contrib.staticfiles.urls import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf import settings

urlpatterns = [
	path('contact/', views.contact, name='contact'),
	path('education/', views.EducationView.as_view(), name='education'),
	path('experience/', views.ExperienceView.as_view(), name='experience'),
	path('', views.index, name='index'),
	]

#urlpatterns += staticfiles_urlpatterns()
#urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
