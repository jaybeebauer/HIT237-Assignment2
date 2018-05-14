from django import forms
from .models import *

class DateInput(forms.DateInput):
    input_type = 'date'

class PriorityForm(forms.ModelForm):
    class Meta:
        model = Priority
        exclude = []
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control'

class TagForm(forms.ModelForm):
    class Meta:
        model = Tag
        exclude = []
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control'

class AssigneeForm(forms.ModelForm):
    class Meta:
        model = Assignee
        exclude = []
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control'

class ItemForm(forms.ModelForm):
    class Meta:
        model = Item
        exclude = []
        widgets = {
            'duedate': DateInput()
        }
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control'