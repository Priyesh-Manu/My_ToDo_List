from django.shortcuts import render,redirect
from .models import MyTask,CompletedTask
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
