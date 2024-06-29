from django.shortcuts import render
from .models import Task


def index(request):
    task=Task.objects.all()
    return render(request,'index.html',{'task':task})

from rest_framework import generics
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from .models import Task
from .serializers import TaskSerializer
from django.utils import timezone

# View for creating a task
class TaskCreate(generics.CreateAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer

# View for listing all tasks
class TaskList(generics.ListAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer

# View for retrieving a single task by ID
class TaskDetail(generics.RetrieveAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer

# View for deleting a task by ID
class TaskDelete(generics.DestroyAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer

# View for tasks due today
class TaskDueToday(generics.ListAPIView):
    serializer_class = TaskSerializer

    def get_queryset(self):
        today = timezone.now().date()
        return Task.objects.filter(due_date=today)
