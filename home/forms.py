from . models import MyTask
from django import forms
class ModelForm(forms.ModelForm):
    
    class Meta :
        model = MyTask
        fields = ('task_name','task_des','task_date')
