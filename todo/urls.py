from django.urls import path
from . import views

urlpatterns = [
    path('todo_list/', views.ReadTODOView.as_view(), name='todo_list'),
    path('todo_list/<int:id>/delete/', views.DeleteTodoView.as_view(), name='delete_todo'),
    path('todo_list/<int:id>/update/', views.UpdateTodoView.as_view(), name='update_todo'),
    path('create_todo/', views.CreateTodoView.as_view(), name='create_todo'),
    path('search_todo/', views.search_todo, name='search_todo'),
]