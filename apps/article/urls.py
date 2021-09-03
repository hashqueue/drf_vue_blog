"""w created urls.py at 2021/9/3 下午12:20"""
from django.urls import path
from article import views

app_name = 'article'

urlpatterns = [
    path('', views.ArticleView.as_view(), name='list_create'),
    path('<int:pk>/', views.ArticleDetailView.as_view(), name='retrieve_update_destroy'),
]
