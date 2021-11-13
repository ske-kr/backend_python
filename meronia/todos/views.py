from django.shortcuts import render
from django.http import JsonResponse

from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import TodoSerializer
from .models import Todo
# Create your views here.

@api_view(['GET'])
def api_main(request):
    f = open('./../VERSION', 'r')
    version = f.readline()
    return JsonResponse(f"TASK API VERSION: {version}", safe=False)

@api_view(['GET'])
def apiOverview(request):
    api_urls = {
        'list, [GET]': '/api/task/todo',
        'create, [POST]': 'api/task/todo',
        'update, [PUT]': 'api/task/todo/<str:id>',
        'delete, [DELETE]': 'api/task/todo/<str:id>',
    }
    return Response(api_urls)

@api_view(['GET'])
def todoList(request):
    todos = Todo.objects.all()
    serializer = TodoSerializer(todos, many=True)
    return Response(serializer.data)

@api_view(['POST'])
def createTodo(request):
    serializer = TodoSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()

    return Response(serializer.data)

@api_view(['DELETE'])
def deleteTodo(request, todo_id: int):
    todo = Todo.objects.get(id=todo_id)
    todo.delete()
    return Response("Successfully deleted")

@api_view(['PUT'])
def updateTodo(request, todo_id: int):
    todo = Todo.objects.get(id=todo_id)
    serializer = TodoSerializer(instance=todo, data=request.data)
    if serializer.is_valid():
        serializer.save()


    return Response(serializer.data)
