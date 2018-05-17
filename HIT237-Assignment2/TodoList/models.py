from django.db import models
import uuid

# Create your models here.

#Priority Model
class Priority(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=20, help_text='Priority type name, ie high or medium')

    def __str__(self):
        return self.name

#Tag Model
class Tag(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=50, help_text='Name of the tag item, ie shopping or family')

    def __str__(self):
        return self.name

#Assignee Model
class Assignee(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    firstname = models.CharField(max_length=100, help_text='The first name of the assignee')
    lastname = models.CharField(max_length=100, help_text='The last name of the assignee')
    email = models.EmailField(help_text='Email of the assignee')

    def __str__(self):
        return str('%s, %s - %s' % (self.lastname, self.firstname, self.email))

#Item Model
class Item(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    title = models.CharField(max_length=100, help_text='The summary of a todo item')
    priority = models.ForeignKey(Priority, help_text='Select a priority to assign to the task')
    tags = models.ManyToManyField(Tag, help_text='Select a tag to assign to the task')
    complete = models.BooleanField(help_text='Whether a todo item is complete or not')
    created = models.DateTimeField(auto_now_add=True, help_text='Date the todo item was created')
    duedate = models.DateField(help_text='Date the todo item is due')
    notes = models.CharField(max_length=250, help_text='Notes on the summary of the todo item')
    assignees = models.ManyToManyField(Assignee)

    def __str__(self):
        return str('%s Due:%s' % (self.title, self.duedate))