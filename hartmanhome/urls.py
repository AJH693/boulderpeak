from django.conf.urls import url
from . import views


urlpatterns = [
	url(r'^$', views.index, name='index'),
	url(r'^about_me/$', views.about_me, name='about_me')
]