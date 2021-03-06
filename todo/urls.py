"""todo URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from mytasks.views import task_view, process_task, active_tasks, completed_tasks, edit_task

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', task_view, name='tasks'),
    path('process-task', process_task, name='process_task'),
    path('active',active_tasks, name='active'),
    path('completed',completed_tasks, name='completed'),
    path('edit/<int:pk>', edit_task, name='edit')
]
