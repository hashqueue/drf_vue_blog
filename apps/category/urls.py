"""w created urls.py at 2021/9/3 下午12:20"""
from django.urls import path, include
from rest_framework import routers
from .views import CategoriesViewSet

router = routers.DefaultRouter()
router.register(prefix=r'categories', viewset=CategoriesViewSet)
urlpatterns = [path('', include(router.urls)), ]
