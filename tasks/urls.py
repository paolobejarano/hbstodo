from django.urls import path
from tasks.views import TaskListCreate, TaskRetrieveUpdateDestroy

urlpatterns = [
    path("api/tasks", TaskListCreate.as_view(), name="task_list_create"),  # Handles GET and POST
    path("api/tasks/<int:pk>", TaskRetrieveUpdateDestroy.as_view(), name="task_retrieve_update_destroy"),  # Handles GET, PUT, PATCH, DELETE
]