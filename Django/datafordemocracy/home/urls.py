from django.conf.urls import url
from . import views

app_name = 'home'

urlpatterns = [
    # /home/
    url(r'^$', views.index, name='index'),
    # /home/about/
    url(r'^about/$', views.about, name='about'),
    # /home/projects/
    url(r'^projects/', views.projects, name='projects'),
    # /home/contactus/
    url(r'^contactus/', views.contactus, name='contactus'),
]