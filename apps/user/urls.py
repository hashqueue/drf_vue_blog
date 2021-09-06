"""w created urls.py at 2021/9/3 下午12:20"""
from django.urls import path, include
from rest_framework import routers
from .views import UsersViewSet, MyTokenObtainPairView, MyTokenRefreshView

router = routers.DefaultRouter()
router.register(prefix=r'users', viewset=UsersViewSet)
urlpatterns = [
    path('', include(router.urls)),
    path('auth/login/', MyTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('auth/token/refresh/', MyTokenRefreshView.as_view(), name='token_refresh'),
]
