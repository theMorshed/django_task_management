from django.shortcuts import render, redirect
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
    
    def get_queryset(self):
        return TaskStoreModel.objects.filter(status='Incomplete')
    
class DisplayCompletedTasks(ListView):
    model = TaskStoreModel
    context_object_name = 'tasks'
    template_name = 'completed_task.html'
    
    def get_queryset(self):
        return TaskStoreModel.objects.filter(status='Complete')
    
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
    
def make_complete(request, pk):
    task = TaskStoreModel.objects.get(id=pk)
    TaskStoreModel(id=pk, title=task.title, desc=task.desc, status='Complete').save()
    return redirect('display_task')
     
class TaskDeleteView(DeleteView):
    model = TaskStoreModel
    template_name = 'delete_confirm.html'
    success_url = reverse_lazy('display_task')