from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from . import models
from django.db.models import Avg
from django.core.paginator import Paginator


#Поиск
def search_view(request):
  query = request.GET.get('s', '')
  blog_list = models.Blog.objects.filter(title__icontains=query) if query else models.Blog.objects.none
  context = {
    'blog_list': blog_list,
    's': query
  }
  return render(request, template_name='blog.html', context=context)




#Вывод всех новостей из модельки Blog но не полностью выводим только название и дату создания поста
def blog_list_view(request):
  if request.method == 'GET':
    blog_list = models.Blog.objects.all().order_by('-id')
    paginator = Paginator(blog_list, 2)
    page = request.GET.get("page")
    page_obj = paginator.get_page(page)
    context = {
      'blog_list': page_obj,
    }
    return render(request, template_name='blog.html', context=context)

#Когда нажимаем кнопку читать подробнее выводит вся информация о данной новости с помощью получения ID
def blog_detail_view(request, id):
  if request.method == 'GET':
    blog_id = get_object_or_404(models.Blog, id=id)
    # Средняя оценка из связанных отзывов
    avg_rating = blog_id.post.aggregate(Avg('mark'))['mark__avg']

    context = {
      'blog_id': blog_id,
      'avg_rating': avg_rating,
    }
    return render(request, template_name='blog_detail.html', context=context)
  





def blog(request):
  if request.method == 'GET':
    return HttpResponse('Привет это мой первый проект на Django!')