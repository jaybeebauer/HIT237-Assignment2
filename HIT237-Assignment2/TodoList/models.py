from django.db import models

# Create your models here.
class Item(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    title = models.CharField(max_length=100, help_text='The summary of a todo item')
    priority = models.ForeignKey(Priority)
    tags = models.ManyToManyField(Tag)
    complete = models.BooleanField(help_text='Whether a todo item is complete or not')
    created = models.DateTimeField(auto_now_add=True, help_text='Date the todo item was created')
    duedate = models.DateField(help_notes='Date the todo item is due')
    notes = models.CharField(max_length=250, help_text='Notes on the summary of the todo item')
    assignees = models.ManyToManyField(Assignee)

    def __str__(self):
        return str('%s Due:%s' % (self.title, dueDate))

class Priority(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=20, help_text='Unqiue identifier for each todo list item')

    def __str__(self):
        return self.name

class Tag(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=50, help_text='Name of the tag item')

    def __str__(self):
        return self.name

class Assignee(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    firstname = models.CharField(max_length=100, help_text='The first name of the assignee')
    lastname = models.CharField(max_length=100, help_text='The last name of the assignee')
    email = models.EmailField(help_text='Email of the assignee')

    def __str__(self):
        return str('%s, %s - %s' % (self.lastname, self.firstname, self.email))