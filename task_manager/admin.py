from django.contrib import admin
from task_manager.models import TaskStoreModel

# Register your models here.
class TaskStoreModelAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'desc']
    
admin.site.register(TaskStoreModel, TaskStoreModelAdmin)
    