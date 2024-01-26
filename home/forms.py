from .models import MyTask
from django import forms

# Define a model form for the MyTask model
class MyTaskForm(forms.ModelForm):
    class Meta:
        model = MyTask
        fields = ('task_name', 'task_des', 'task_date')
