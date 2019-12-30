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

    # #all button at the bottom
    # if cmd == "all":
    #     all_tasks = Task.objects.all()
    #     tasks =[]
    #     for task in all_tasks:
    #         tasks.append()
    # return HttpResponseRedirect('/')

    # # active button at the bottom
    # if cmd == "active":
    #     all_tasks = Task.objects.all()
    #     tasks =[]
    #     for task in all_tasks:
    #         if task.status == False:
    #             tasks.append()
    # return HttpResponseRedirect('/')
        
    # # completed button at the bottom
    # if cmd == "completed":
    #     all_tasks = Task.objects.all()
    #     tasks =[]
    #     for task in all_tasks:
    #         if task.status == True:
    #             tasks.append()
    # return HttpResponseRedirect('/')
