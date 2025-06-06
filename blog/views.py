from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from . import models


#Вывод всех новостей из модельки Blog но не полностью выводим только название и дату создания поста
def blog_list_view(request):
  if request.method == 'GET':
    blog_list = models.Blog.objects.all().order_by('-id')
    context = {
      'blog_list': blog_list,
    }
    return render(request, template_name='blog.html', context=context)

#Когда нажимаем кнопку читать подробнее выводит вся информация о данной новости с помощью получения ID
def blog_detail_view(request, id):
  if request.method == 'GET':
    blog_id = get_object_or_404(models.Blog, id=id)
    context = {
      'blog_id': blog_id,
    }
    return render(request, template_name='blog_detail.html', context=context)
  





def blog(request):
  if request.method == 'GET':
    return HttpResponse('Привет это мой первый проект на Django!')