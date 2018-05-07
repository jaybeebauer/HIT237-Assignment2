from django.shortcuts import render
from TodoList.models import *
from TodoList.forms import *
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
import re

# Create your views here.
def home(request):
    return render(request, 'index.html')

def list(request, type):
    results = GetAllModelObjects(type.title())
    page_data = {'list' : results, 'type' : type}
    return render(request, 'list.html', page_data)

def detail(request, type, guid):
    result = GetModelDetail(type.title(), guid)
    page_data = {'item' : result, 'type' : type}
    return render(request, 'detail.html', page_data)

def record(request, operation, type, guid=''):
    if operation == 'create':
        if request.method != 'POST':
            page_data = {'form' : eval("%sForm()" % (type.title(),)), 'operation' : operation, 'type' : type}
        else:
            form = eval("%sForm(request.POST)" % (type.title(),))
            if form.is_valid() != True:
                page_data = {'form' : form, 'operation' : operation, 'type' : type}
            else:
                cleanform = form.cleaned_data
                new_item = form.save()
                return HttpResponseRedirect(reverse('list', args=(type,)))
    elif operation == 'update':
        record = eval("%s.objects.get(id='%s')" % (type.title(), guid))
        if request.method != 'POST':
            form = eval("%sForm(instance=record)" % (type.title(),))
            page_data = {'form' : form, 'operation' : operation, 'type' : type, 'guid' : guid}
        else:
            form = eval("%sForm(request.POST, instance=record)" % (type.title(),))
            if form.is_valid() != True:
                page_data = {'form' : form, 'operation' : operation, 'type' : type, 'guid' : guid}
            else:
                form.save()
                return HttpResponseRedirect(reverse('list', args=(type,)))
    elif operation == 'detail':
        record = GetModelDetail(type.title(), guid)
        page_data = {'record' : record, 'operation' : operation, 'type' : type, 'guid' : guid}
    elif operation == 'delete':
        if type == 'item':
            record = Item.objects.get(id=guid)
            record.delete()
            page_data = {'operation' : operation, 'type' : type, 'guid' : guid}
        if type == 'priority':
            record = Priority.objects.get(id=guid)
            record.delete()
            page_data = {'operation' : operation, 'type' : type, 'guid' : guid}
        if type == 'tag':
            record = Tag.objects.get(id=guid)
            record.delete()
            page_data = {'operation' : operation, 'type' : type, 'guid' : guid}
        if type == 'assignee':
            record = Assignee.objects.get(id=guid)
            record.delete()
            page_data = {'operation' : operation, 'type' : type, 'guid' : guid}

    return render(request, 'record.html', page_data)

def GetAllModelObjects(type):
    result = eval("%s.objects.all()" % (type))
    return result

def GetModelDetail(type, guid):
    result = eval("%s.objects.get(id='%s')" % (type, guid))
    return result