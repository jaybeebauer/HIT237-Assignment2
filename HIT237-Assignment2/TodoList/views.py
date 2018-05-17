from django.shortcuts import render
from TodoList.models import *
from TodoList.forms import *
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
import re

# Create your views here.
def home(request):
    return render(request, 'index.html')

#List items or assignees or tags or prioritys and display in template
def list(request, type):
    if type == 'item':
        #If type is item, get all objcets sort by complete, and then by duedate
        results = Item.objects.all().order_by('complete', 'duedate')
    else:
        #If any other type, create function dynamicly, grab all objects
        results = eval("%s.objects.all()" % (type.title()))
    #Fill variable papge_data with the list results of all objects and the type of list item
    page_data = {'list' : results, 'type' : type}
    return render(request, 'list.html', page_data)

def record(request, operation, type, guid=''):
    if operation == 'create':
        #If create has been chosen as operation go here
        if request.method != 'POST':
            #If form has not been submited show the form as new and send to template
            page_data = {'form' : eval("%sForm()" % (type.title(),)), 'operation' : operation, 'type' : type}
        else:
            #If the form has been submitted, lets get results out of the POST variable create form function to use (which form type)
            form = eval("%sForm(request.POST)" % (type.title(),))
            if form.is_valid() != True:
                #If form has errors (not filled in or missing data) send back to template and ask user to fix issues
                page_data = {'form' : form, 'operation' : operation, 'type' : type}
            else:
                form.save()
                #Once saved send user back to the list with the new item
                return HttpResponseRedirect(reverse('list', args=(type,)))
    elif operation == 'update':
        #If update has been chosen as operation go here
        record = GetModelDetail(type, guid)
        if request.method != 'POST':
            #If form has not been submited get form data for guid, show the form as update and send to template
            page_data = {'form' : eval("%sForm(instance=record)" % (type.title(),)), 'operation' : operation, 'type' : type, 'guid' : guid}
        else:
            #If the form has been submitted, lets get results out of the POST variable create form function to use (which form type)
            form = eval("%sForm(request.POST, instance=record)" % (type.title(),))
            if form.is_valid() != True:
                #If form has errors (not filled in or missing data) send back to template and ask user to fix issues
                page_data = {'form' : form, 'operation' : operation, 'type' : type, 'guid' : guid}
            else:
                form.save()
                #Once saved send user back to the list with the new item
                return HttpResponseRedirect(reverse('list', args=(type,)))
    elif operation == 'detail':
        #If detail has been chosen as operation go here
        record = GetModelDetail(type, guid)
        #Fill variable papge_data with the list results of all parts of each item, the type, operation and the guid
        page_data = {'record' : record, 'operation' : operation, 'type' : type, 'guid' : guid}
    elif operation == 'delete':
        #If delete has been chosen as operation go here
        record = GetModelDetail(type,guid)
        #Fill variable papge_data with the list results of all parts of each item, the type, operation and the guid
        page_data = {'record' : record, 'operation' : operation, 'type' : type, 'guid' : guid}
        #Delete record
        record.delete()
    return render(request, 'record.html', page_data)

#This function creates function to get all objects for a give type and GUID ie, Tag.objects.get(id=guid)
def GetModelDetail(type, guid):
    result = eval("%s.objects.get(id='%s')" % (type.title(), guid))
    return result