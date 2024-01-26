from django.contrib import admin
from . import models

# Register your models here.
class my_task(admin.ModelAdmin):
    list_display =['user','task_name','task_date',]
admin.site.register(models.MyTask,my_task)

class completed_task(admin.ModelAdmin):
    list_display =['user','completed_task_name','completed_task_date',]
admin.site.register(models.CompletedTask,completed_task)
class contact_message(admin.ModelAdmin):
    list_display =['email','message_date','message_replied',]
    list_editable=['message_replied',]
admin.site.register(models.Contact,contact_message)