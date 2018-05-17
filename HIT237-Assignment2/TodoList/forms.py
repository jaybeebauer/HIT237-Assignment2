from django import forms
from .models import *

class DateInput(forms.DateInput):
    #This class adds the date data type (HTML) for the date field, so in modern browser it will show a calandar instead of just text field
    input_type = 'date'

class PriorityForm(forms.ModelForm):
    class Meta:
        model = Priority
        exclude = []
    #This function goes through each visable on form initilasation field in the model and adds class form-control to it
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