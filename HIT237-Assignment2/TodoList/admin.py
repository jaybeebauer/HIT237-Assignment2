from django.contrib import admin
from TodoList.models import *

# Register your models here.
admin.site.register(Item)
admin.site.register(Priority)
admin.site.register(Tag)
admin.site.register(Assignee)