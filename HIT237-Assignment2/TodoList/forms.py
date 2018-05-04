from django import forms
from .models import *

class DateInput(forms.DateInput):
    input_type = 'date'

class PriorityForm(forms.ModelForm):
    class Meta:
        model = Priority
        exclude = []

class TagForm(forms.ModelForm):
    class Meta:
        model = Tag
        exclude = []

class AssigneeForm(forms.ModelForm):
    class Meta:
        model = Assignee
        exclude = []

class ItemForm(forms.ModelForm):
    class Meta:
        model = Item
        exclude = []
        widgets = {
            'duedate': DateInput()
        }