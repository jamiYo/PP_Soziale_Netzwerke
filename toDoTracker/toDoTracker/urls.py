from django.urls import path

from . import views


app_name = 'toDoTracker'
urlpatterns = [
    path('myToDos/', views.mytodos, name='myToDos'),
    path('myToDos/add/', views.add, name='add'),
    path('myToDos/impressum/', views.impressum, name='impressum'),
    path('myToDos/delete/todo<int:todo_id>/', views.delete, name='delete'),
    path('myToDos/edit/todo<int:todo_id>/', views.edit, name='edit'),
]