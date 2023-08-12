from django.contrib import admin
from . import models 

# Register your models here.
@admin.register(models.taskModel)
class taskModelAdmin(admin.ModelAdmin):
    list_display = ('taskNo', 'taskTitle', 'taskDescription', 'is_completed')
# admin.site.register(models.taskModel)