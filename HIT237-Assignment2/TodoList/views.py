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
                form.save()
                return HttpResponseRedirect(reverse('list', args=(type,)))
    elif operation == 'update':
        record = GetModelDetail(type, guid)
        if request.method != 'POST':
            page_data = {'form' : eval("%sForm(instance=record)" % (type.title(),)), 'operation' : operation, 'type' : type, 'guid' : guid}
        else:
            form = eval("%sForm(request.POST, instance=record)" % (type.title(),))
            if form.is_valid() != True:
                page_data = {'form' : form, 'operation' : operation, 'type' : type, 'guid' : guid}
            else:
                form.save()
                return HttpResponseRedirect(reverse('list', args=(type,)))
    elif operation == 'detail':
        record = GetModelDetail(type, guid)
        page_data = {'record' : record, 'operation' : operation, 'type' : type, 'guid' : guid}
    elif operation == 'delete':
        record = GetModelDetail(type,guid)
        page_data = {'record' : record, 'operation' : operation, 'type' : type, 'guid' : guid}
        record.delete()       
    return render(request, 'record.html', page_data)

def GetAllModelObjects(type):
    result = eval("%s.objects.all()" % (type))
    return result

def GetModelDetail(type, guid):
    result = eval("%s.objects.get(id='%s')" % (type.title(), guid))
    return result