from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView

from tasks.serializers import TaskSerializer
from tasks.models import Task


# GET and POST api/tasks
class TaskListCreate(ListCreateAPIView):
    """Handles listing all tasks (GET) and creating a new task (POST)"""
    serializer_class = TaskSerializer
    queryset = Task.objects.all()


# GET, PUT, PATCH, DELETE api/tasks/<int:pk>
class TaskRetrieveUpdateDestroy(RetrieveUpdateDestroyAPIView):
    """Handles retrieving a task (GET), updating it (PUT/PATCH), and deleting it (DELETE)"""
    serializer_class = TaskSerializer
    queryset = Task.objects.all()
    lookup_field = 'pk'
