from django.shortcuts import render,redirect
from .models import MyTask,CompletedTask,Contact
from . forms import ModelForm
# Create your views here.
from django.contrib.auth.decorators import login_required

@login_required
def home(request):
    tasks = {
        'my_task': MyTask.objects.filter(user=request.user),
        'com_task': CompletedTask.objects.filter(user=request.user),
    }
    if request.method == 'POST':
        task_name = request.POST['name']
        task_des = request.POST['description']
        task_date = request.POST['date']
        user_task = MyTask(user=request.user, task_name=task_name, task_des=task_des, task_date=task_date)
        user_task.save()
        return redirect('/')
    return render(request, 'index.html', tasks)
@login_required
def completed_task(request, id):
    obj = MyTask.objects.get(id=id)
    
    com_task = CompletedTask(
        user=obj.user,
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

@login_required
def redo_completed_task(request, id): 
    obj = CompletedTask.objects.get(id=id)
    
    redo_com_task = MyTask(
        user = obj.user,
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

def contact(request):
    if request.method =='POST':
        email = request.POST['contactemail']
        contact_message = request.POST['contactmsg']
        user = Contact(email=email,message=contact_message)
        user.save()
        return redirect('home')
    return render(request,'contact.html')

def about(request):
    return render(request,'about.html')