from django.db import models
from django.contrib.auth.models import User
import datetime

# Create your models here.

# Model for tasks that are not completed
class MyTask(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    task_name = models.CharField(max_length=100)
    task_des = models.TextField()
    task_date = models.DateField(default=datetime.date.today)

    def __str__(self):
        return self.task_name

# Model for tasks that are marked as completed
class CompletedTask(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    completed_task_name = models.CharField(max_length=100)
    completed_task_des = models.TextField()
    completed_task_date = models.DateField(default=datetime.date.today)

    def __str__(self):
        return self.completed_task_name

# Model for storing contact messages
class Contact(models.Model):
    email = models.EmailField(max_length=254)
    message = models.TextField()
    message_date = models.DateField(auto_now=True)
    message_replied = models.BooleanField(default=False)
