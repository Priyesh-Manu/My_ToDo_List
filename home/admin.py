from django.contrib import admin
from . import models

# Register your models here.

admin.site.register(models.MyTask)
admin.site.register(models.CompletedTask)
class contact_message(admin.ModelAdmin):
    list_display =['email','message_date','message_replied',]
    list_editable=['message_replied',]
admin.site.register(models.Contact,contact_message)