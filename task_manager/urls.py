from django.urls import path
from task_manager.views import DisplayTasksListView, AddTaskFormView, TaskUpdateView, TaskDeleteView

urlpatterns = [
    path('', DisplayTasksListView.as_view(), name='display_task'),
    path('add_task/', AddTaskFormView.as_view(), name='add_task'),
    path('edit_task/<int:pk>', TaskUpdateView.as_view(), name='edit_task'),
    path('delete_task/<int:pk>', TaskDeleteView.as_view(), name='delete_book'),
]
