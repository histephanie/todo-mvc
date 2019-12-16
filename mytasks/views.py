from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def task_view(request):
    return render(request,'tasks.html')
