from django.db import models
import datetime
# Create your models here.
class MyTask(models.Model):
    task_name = models.CharField(max_length=100)
    task_des = models.TextField()
    task_date = models.DateField(default=datetime.date.today)
    
    def __str__(self):
        return self.task_name
    
class CompletedTask(models.Model):
    completed_task_name = models.CharField(max_length=100)
    completed_task_des = models.TextField()
    completed_task_date = models.DateField(default=datetime.date.today)
    
    def __str__(self):
        return self.completed_task_name

class Contact(models.Model):
    email = models.EmailField(max_length=254)
    message=models.TextField()
    message_date = models.DateField(auto_now=True)
    message_replied = models.BooleanField(default=False)
    
    