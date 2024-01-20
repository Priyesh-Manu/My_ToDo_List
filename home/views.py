from django.shortcuts import render,redirect
from .models import MyTask
# Create your views here.

def home(request):
    tasks={
        'my_task':MyTask.objects.all()
    }
    if request.method=='POST':
        task_name = request.POST['name']
        task_des = request.POST['description']
        task_date = request.POST['date']
        user = MyTask(task_name=task_name,task_des=task_des,task_date=task_date)
        user.save()
        return redirect ('/')
    return render(request,'index.html',tasks)