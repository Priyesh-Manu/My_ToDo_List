from django.db import models
import datetime
# Create your models here.
class MyTask(models.Model):
    task_name = models.CharField(max_length=100)
    task_des = models.TextField()
    task_date = models.DateField(default=datetime.date.today)
    
    def __str__(self):
        return self.task_name