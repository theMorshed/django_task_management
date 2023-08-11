from django import forms
from task_manager.models import TaskStoreModel

class TaskStoreForm(forms.ModelForm):
    class Meta:
        model = TaskStoreModel
        fields = ['title', 'desc']
    