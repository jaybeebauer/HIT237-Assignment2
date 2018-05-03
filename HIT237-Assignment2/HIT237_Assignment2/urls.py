"""
Definition of urls for HIT237_Assignment2.
"""

from django.conf.urls import include, url
from django.contrib import admin
from TodoList import views

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', views.home, name='home'),
    url(r'^todolist/?$', views.todolist, name='todolist'),
    url(r'^todolist/item/create/?$', views.adjustrecord, name='create'),
    url(r'^todolist/item/update/?$', views.adjustrecord, name='update'),
    url(r'^todolist/item/detail/?$', views.adjustrecord, name='detail'),
    url(r'^todolist/item/delete/?$', views.adjustrecord, name='delete'),
]
