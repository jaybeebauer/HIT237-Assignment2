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
]
