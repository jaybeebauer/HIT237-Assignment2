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
    url(r'^assignees/?$', views.assignees, name='assignees'),
    url(r'^priorities/?$', views.priorities, name='priorities'),
    url(r'^tags/?$', views.tags, name='tags'),
    url(r'^(create)/(item|assignee|priority|tag)/$', views.record, name='create'),
    url(r'^(?i)(update|detail|delete)/(item|assignee|priority|tag)/([a-z0-9]{8}-[a-z0-9]{4}-[a-z0-9]{4}-[a-z0-9]{4}-[a-z0-9]{12})/?', views.record, name='record'),

]
