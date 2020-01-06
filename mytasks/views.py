from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .models import Task

# Create your views here.
def task_view(request):
    all_tasks = Task.objects.all() 
    active_count = 0
    for task in all_tasks:
        if task.status == False:
            active_count += 1
    filter_type = "all"
    return render(request,'tasks.html', {'tasks':all_tasks, 'filter_type':filter_type, 'active_count':active_count})


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
 
    #the "x" next to each task
    if cmd == "delete":
        task = Task(pk=request.POST['task_id'])
        task.delete()
        return HttpResponseRedirect('/')

    #clear completed button bottom right
    if cmd == "clear":
        all_tasks = Task.objects.all() 
        for task in all_tasks:
            if task.status == True:
                task.delete()
        return HttpResponseRedirect('/')

    #the check mark next to each task
    if cmd == "check":
        task = Task.objects.get(pk=request.POST['task_id'])
        task.status = not task.status
        task.save()
        return HttpResponseRedirect('/')

def active_tasks(request):
    active_tasks = Task.objects.filter(status=False)
    filter_type = "active"
    return render(request,'tasks.html', {'tasks':active_tasks, 'filter_type':filter_type})


def completed_tasks(request):
    completed_tasks = Task.objects.filter(status=True)
    filter_type = "completed"
    return render(request,'tasks.html', {'tasks':completed_tasks, 'filter_type':filter_type})

# pk is a parameter so that the func knows wich task is being edited, 
# the value for the pk comes from urls.py 
# then the tasks.html link also has the pk that it takes from the current task
def edit_task(request, pk):
    if request.method == 'GET':
        task = Task.objects.get(pk=pk)
        return render(request, 'edit.html', {'task':task})
        
    elif request.method == 'POST':
        task = Task.objects.get(pk=pk)
        task.title = request.POST['title']
        task.save()
        return HttpResponseRedirect('/')
