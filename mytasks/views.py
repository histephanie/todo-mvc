from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .models import Task

# Create your views here.
def task_view(request):
    all_tasks = Task.objects.all() 
    return render(request,'tasks.html', {'tasks':all_tasks})

def new_task(request):
    new_task = Task(title=request.POST['title'])
    new_task.save()
    return HttpResponseRedirect('/')
