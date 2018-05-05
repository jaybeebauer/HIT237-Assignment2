from django.shortcuts import render
from TodoList.models import *
from TodoList.forms import *
import re

# Create your views here.
def home(request):
    return render(request, 'index.html')

def list(request, type):
    results = GetAllModelObjects(type.title())
    page_data = {'list': results}
    return render(request, 'list.html', page_data)

def record(request, operation, type, guid=''):
    page_data = ''
    if operation == 'create':
        if type == 'item':
            page_data = {'form' : ItemForm(), 'operation' : operation, 'type' : type}
        if type == 'priority':
            page_data = {'form' : PriorityForm(), 'operation' : operation, 'type' : type}
        if type == 'tag':
            page_data = {'form' : TagForm(), 'operation' : operation, 'type' : type}
        if type == 'assignee':
            page_data = {'form' : AssigneeForm(), 'operation' : operation, 'type' : type}
    elif operation == 'update':
        if type == 'item':
            record = Item.objects.get(id=guid)
            form = ItemForm(instance=record)
            page_data = {'form' : form, 'operation' : operation, 'type' : type}
        if type == 'priority':
            record = Priority.objects.get(id=guid)
            form = PriorityForm(instance=record)
            page_data = {'form' : form, 'operation' : operation, 'type' : type}
        if type == 'tag':
            record = Tag.objects.get(id=guid)
            form = TagForm(instance=record)
            page_data = {'form' : form, 'operation' : operation, 'type' : type}
        if type == 'assignee':
            record = Assignee.objects.get(id=guid)
            form = AssigneeForm(instance=record)
            page_data = {'form' : form, 'operation' : operation, 'type' : type}
    elif operation == 'detail':
        if type == 'item':
            record = Item.objects.get(id=guid)
            form = ItemForm(instance=record)
            page_data = {'form' : form, 'operation' : operation, 'type' : type}
    elif operation == 'delete':
        if type == 'item':
            record = Item.objects.get(id=guid)
            record.delete()
            page_data = {'operation' : operation, 'type' : type}
        if type == 'priority':
            record = Priority.objects.get(id=guid)
            record.delete()
            page_data = {'operation' : operation, 'type' : type}
        if type == 'tag':
            record = Tag.objects.get(id=guid)
            record.delete()
            page_data = {'operation' : operation, 'type' : type}
        if type == 'assignee':
            record = Assignee.objects.get(id=guid)
            record.delete()
            page_data = {'operation' : operation, 'type' : type}

    return render(request, 'record.html', page_data)

def GetAllModelObjects(operation):
    result = eval("%s.objects.all()" % (operation))
    return result