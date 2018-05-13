from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse

from .models import ToDo


def mytodos(request):
    todo_queryset = ToDo.objects.all().order_by('due_date')
    context = {'todo_queryset' : todo_queryset}
    return render(request, 'toDoTracker/index.html', context)


def delete(request, todo_id):
    item = get_object_or_404(ToDo, pk=todo_id)
    item.delete()
    return redirect(reverse('toDoTracker:myToDos'))


def add(request):
    if request.method == "GET":
        return render(request, 'toDoTracker/addTODO.html')
    elif request.method == "POST":
        ToDo.objects.create(toDo_text=request.POST['todo_text'], due_date=request.POST['date'],\
                            progress=request.POST['progress'])
        return redirect(reverse('toDoTracker:myToDos'))


def edit(request, todo_id):
    if request.method == "GET":
        item = get_object_or_404(ToDo, pk=todo_id)
        return render(request, 'toDoTracker/editTODO.html', {'item' :item})
    elif request.method == "POST":
        ToDo.objects.filter(id=todo_id).update(toDo_text=request.POST['todo_text'], due_date=request.POST['date'],
                                               progress=request.POST['progress'])
        return redirect(reverse('toDoTracker:myToDos'))


def impressum(request):
    return render(request, 'toDoTracker/impressum.html')
