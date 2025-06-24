from django.shortcuts import render, redirect, get_object_or_404
from . import models, forms
#CRUD  - CREATE READ UPDATE DELETE
from django.views import generic


def search_todo(request):
    query = request.GET.get('q', '')
    todo_lst = models.TodoModel.objects.filter(task__icontains = query) if query else models.TodoModel.objects.none
    context = {
        'q': query,
        'todo_lst': todo_lst
    }
    return render(request, template_name='todo_lst.html', context=context)


#CREATE CBV
class CreateTodoView(generic.CreateView):
    model = models.TodoModel
    form_class = forms.TodoForm
    template_name = 'create_todo.html'
    success_url = '/todo_list/'


# def create_todo_view(request):
#     if request.method == 'POST':
#         form = forms.TodoForm(request.POST, request.FILES)
#         if form.is_valid():
#             form.save()
#             return redirect('todo_list')
#     else:
#         form = forms.TodoForm()

#     return render(request, template_name='create_todo.html',
#                   context={'form': form})  

##READ 
class ReadTODOView(generic.ListView):
    model = models.TodoModel
    template_name = 'todo_lst.html'
    context_object_name = 'todo_lst'



# def read_todo_view(request):
#     if request.method == 'GET':
#         todo_lst = models.TodoModel.objects.all()
#         context = {'todo_lst': todo_lst}
#         return render(request, 'todo_lst.html', context=context)



##DELETE TO DO
class DeleteTodoView(generic.DeleteView):
    template_name = 'confirm_delete.html'
    success_url = '/todo_list/'

    def get_object(self, *args, **kwargs):
        todo_id = self.kwargs.get('id')
        return get_object_or_404(models.TodoModel, id=todo_id)
    

# def delete_todo_view(request, id):
#     todo_id = get_object_or_404(models.TodoModel, id=id)
#     todo_id.delete()
#     return redirect('todo_list')


##Update To do
class UpdateTodoView(generic.UpdateView):
    model = models.TodoModel
    form_class = forms.TodoForm
    template_name = 'update_todo.html'
    success_url = '/todo_list/'
    
    def get_object(self, *args, **kwargs):
        todo_id = self.kwargs.get('id')
        return get_object_or_404(models.TodoModel, id=todo_id)
    
    def form_valid(self, form):
        print(form.cleaned_data)
        return super(UpdateTodoView, self).form_valid(form=form)




# def update_todo_view(request, id):
#     todo_id = get_object_or_404(models.TodoModel, id=id)
#     if request.method == 'POST':
#         form = forms.TodoForm(request.POST, instance=todo_id)
#         if form.is_valid():
#             form.save()
#             return redirect('todo_list')
#     else:
#         form = forms.TodoForm(instance=todo_id)
    
#     return render(request, template_name='update_todo.html',
#                   context={
#                       'form': form,
#                       'todo_id': todo_id, 
#                   })
