from rest_framework.exceptions import NotFound
from rest_framework.response import Response
from rest_framework import status
from plugin_sample_app.serializers import TaskSerializer
from plugin_sample_app.models import Task
from rest_framework import generics

tasks = [
    Task(title="task 1", description="test description 1"),
    Task(title="task 2", description="test description 2"),
    Task(title="task 3", description="test description 3"),
]


class TaskListView(generics.ListCreateAPIView):
    def list(self, request, *args, **kwargs):
        data = [task.serialize() for task in tasks]
        return Response(data=data)

    def create(self, request, *args, **kwargs):
        serializer = TaskSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        data = serializer.validated_data
        task = Task(**data)
        tasks.append(task)
        return Response(task.serialize(), status=status.HTTP_201_CREATED)


class TaskDetailView(generics.RetrieveUpdateDestroyAPIView):
    def retrieve(self, request, *args, **kwargs):
        object_id = kwargs.get("id")
        matching_tasks = [task for task in tasks if task.id == object_id]
        if matching_tasks == []:
            raise NotFound()
        task = matching_tasks[0]
        return Response(task.serialize())

    def update(self, request, *args, **kwargs):
        object_id = kwargs.get("id")
        matching_tasks = [task for task in tasks if task.id == object_id]
        if matching_tasks == []:
            raise NotFound()
        task = matching_tasks[0]
        serializer = TaskSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        task.update(serializer.validated_data)
        return Response(task.serialize())

    def destroy(self, request, *args, **kwargs):
        object_id = kwargs.get("id")
        matching_tasks = [task for task in tasks if task.id == object_id]
        if matching_tasks == []:
            raise NotFound()
        task = matching_tasks[0]
        tasks.remove(task)
        return Response(status=status.HTTP_204_NO_CONTENT)
