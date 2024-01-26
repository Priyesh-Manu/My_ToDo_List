from django.contrib import admin
from . import models

# Register your models here.

# Customizing the admin display for the MyTask model
class MyTaskAdmin(admin.ModelAdmin):
    list_display = ['user', 'task_name', 'task_date']

admin.site.register(models.MyTask, MyTaskAdmin)

# Customizing the admin display for the CompletedTask model
class CompletedTaskAdmin(admin.ModelAdmin):
    list_display = ['user', 'completed_task_name', 'completed_task_date']

admin.site.register(models.CompletedTask, CompletedTaskAdmin)

# Customizing the admin display for the Contact model
class ContactMessageAdmin(admin.ModelAdmin):
    list_display = ['email', 'message_date', 'message_replied']
    list_editable = ['message_replied']

admin.site.register(models.Contact, ContactMessageAdmin)
