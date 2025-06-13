from django.urls import path
from . import views

urlpatterns = [
  path('', views.blog_list_view, name='news_posts'),
  path('news_posts/<int:id>/', views.blog_detail_view, name='news_posts_detail'),
  path('blog/', views.blog, name='blog'),
]