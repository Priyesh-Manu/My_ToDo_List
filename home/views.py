from django.shortcuts import render,redirect
from .models import MyTask,CompletedTask
from . forms import ModelForm
# Create your views here.

def home(request):
    tasks={
        'my_task':MyTask.objects.all(),
        'com_task':CompletedTask.objects.all(),
    }
    if request.method=='POST':
        task_name = request.POST['name']
        task_des = request.POST['description']
        task_date = request.POST['date']
        user = MyTask(task_name=task_name,task_des=task_des,task_date=task_date)
        user.save()
        return redirect ('/')
    return render(request,'index.html',tasks)

def completed_task(request, id):
    obj = MyTask.objects.get(id=id)
    
    com_task = CompletedTask(
        completed_task_name=obj.task_name,
        completed_task_des=obj.task_des,
        completed_task_date=obj.task_date
    )
    com_task.save()
    obj.delete()
    return redirect('home')

def delete_completed_task(request, id):  # Rename the parameter to avoid conflict
    obj = CompletedTask.objects.get(id=id)
    obj.delete()
    return redirect('home')

def redo_completed_task(request, id): 
    obj = CompletedTask.objects.get(id=id)
    
    redo_com_task = MyTask(
        task_name=obj.completed_task_name,
        task_des=obj.completed_task_des,
        task_date=obj.completed_task_date
    )
    redo_com_task.save()
    obj.delete()
    return redirect('home')

def edit_task(request, id):
    obj = MyTask.objects.get(id=id)
    Forms = ModelForm(request.POST or None, request.FILES, instance=obj)

    if request.method == 'POST':
        if Forms.is_valid():
            Forms.save()
            return redirect('home')

    form_new = {
        'obj': obj,
        'form': Forms
    }
    return render(request, 'edit.html', form_new)
