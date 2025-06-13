from django.shortcuts import render, redirect, get_object_or_404
from . import models, forms
#CRUD  - CREATE READ UPDATE DELETE

def create_todo_view(request):
    if request.method == 'POST':
        form = forms.TodoForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('todo_list')
    else:
        form = forms.TodoForm()

    return render(request, template_name='create_todo.html',
                  context={'form': form})  


def read_todo_view(request):
    if request.method == 'GET':
        todo_lst = models.TodoModel.objects.all()
        context = {'todo_lst': todo_lst}
        return render(request, 'todo_lst.html', context=context)


def delete_todo_view(request, id):
    todo_id = get_object_or_404(models.TodoModel, id=id)
    todo_id.delete()
    return redirect('todo_list')

def update_todo_view(request, id):
    todo_id = get_object_or_404(models.TodoModel, id=id)
    if request.method == 'POST':
        form = forms.TodoForm(request.POST, instance=todo_id)
        if form.is_valid():
            form.save()
            return redirect('todo_list')
    else:
        form = forms.TodoForm(instance=todo_id)
    
    return render(request, template_name='update_todo.html',
                  context={
                      'form': form,
                      'todo_id': todo_id, 
                  })
