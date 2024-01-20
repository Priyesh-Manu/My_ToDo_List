from django.contrib import admin
from . import models

# Register your models here.

admin.site.register(models.MyTask)
admin.site.register(models.CompletedTask)