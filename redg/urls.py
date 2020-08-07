from django.urls import path

from . import views

urlpatterns = [
	path('', views.index, name='index'),
	path('f/<int:finding_id>', views.show_finding, name='f'),
]