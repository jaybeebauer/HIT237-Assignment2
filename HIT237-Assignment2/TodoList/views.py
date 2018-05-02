from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, 'index.html')

def todolist(request):
    #Add function here
    return render(request, 'todolist.html')

def adjustrecord(request):
    #Add function here
    return render(request, 'adjustrecord.html')