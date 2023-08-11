from django.contrib import admin
from task_manager.models import TaskStoreModel

# Register your models here.
class TaskStoreModelAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'desc', 'status']
    
admin.site.register(TaskStoreModel, TaskStoreModelAdmin)
    