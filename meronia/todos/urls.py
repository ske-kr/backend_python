from django.urls import path
from . import views

urlpatterns = [
    path("", views.api_main, name='version'),
    path("list", views.apiOverview, name='api-overview'),
    path("todo", views.todoList, name='todo-overview'),
    path("todo/create", views.createTodo, name='todo-create'),
    path("todo/update/<int:todo_id>", views.updateTodo, name='todo-update'),
    path("todo/delete/<int:todo_id>", views.deleteTodo, name='todo-delete'),
]
