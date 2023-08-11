from django.urls import path
from task_manager.views import DisplayTasksListView, AddTaskFormView, TaskUpdateView, TaskDeleteView, DisplayCompletedTasks, make_complete

urlpatterns = [
    path('', DisplayTasksListView.as_view(), name='display_task'),
    path('completed_task/', DisplayCompletedTasks.as_view(), name='completed_task'),
    path('add_task/', AddTaskFormView.as_view(), name='add_task'),
    path('complete/<int:pk>', make_complete, name='make_complete'),
    path('edit_task/<int:pk>', TaskUpdateView.as_view(), name='edit_task'),
    path('delete_task/<int:pk>', TaskDeleteView.as_view(), name='delete_book'),
]
