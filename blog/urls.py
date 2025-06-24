from django.urls import path
from . import views

urlpatterns = [
  path('', views.BlogListView.as_view(), name='news_posts'),
  path('news_posts/<int:id>/', views.BlogDetailView.as_view(), name='news_posts_detail'),
  path('blog/', views.BlogView.as_view(), name='blog'),
  path('search/', views.SearchView.as_view(), name='search'),
]