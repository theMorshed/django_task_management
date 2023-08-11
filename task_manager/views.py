from django.shortcuts import render
from django.views.generic import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from task_manager.models import TaskStoreModel
from django.urls import reverse_lazy
from task_manager.forms import TaskStoreForm

# Create your views here.
class DisplayTasksListView(ListView):
    model = TaskStoreModel
    context_object_name = 'tasks'
    template_name = 'display_task.html'
    
class AddTaskFormView(CreateView):
    model = TaskStoreModel
    form_class = TaskStoreForm
    template_name = 'add_task.html'
    success_url = reverse_lazy('display_task')
    
class TaskUpdateView(UpdateView):
    model = TaskStoreModel
    template_name = 'add_task.html'
    form_class = TaskStoreForm
    success_url = reverse_lazy('display_task')
    
class TaskDeleteView(DeleteView):
    model = TaskStoreModel
    template_name = 'delete_confirm.html'
    success_url = reverse_lazy('display_task')