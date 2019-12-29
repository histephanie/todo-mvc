from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .models import Task

# Create your views here.
def task_view(request):
    all_tasks = Task.objects.all() 
    return render(request,'tasks.html', {'tasks':all_tasks})


def process_task(request):
    cmd = request.POST['cmd']

    if cmd == "new_task":
        new_task = Task(title=request.POST['title'])
        new_task.save()
        return HttpResponseRedirect('/')

    if cmd == "status":
        task = Task(pk=request.POST['task_id'])
        task.status = not task.status
        task.save()
        return HttpResponseRedirect('/')

    if cmd == "toggle_all":
        all_tasks = Task.objects.all() 
        for task in all_tasks:
            task.status = not task.status
            task.save()
        return HttpResponseRedirect('/')
 
    if cmd == "delete":
        task = Task(pk=request.POST['task_id'])
        task.delete()
        return HttpResponseRedirect('/')

    #clear completed button
    if cmd == "clear":
        all_tasks = Task.objects.all() 
        for task in all_tasks:
            if task.status == True:
                task.delete()
        return HttpResponseRedirect('/')

    if cmd == "check":
        task = Task.objects.get(pk=request.POST['task_id'])
        task.status = not task.status
        task.save()
        return HttpResponseRedirect('/')
