from rest_framework import viewsets
from .models import Category
from utils.drf_utils.custom_permissions import IsAdminOrReadOnly
from .serializers import CategoriesSerializer, CategoriesDetailSerializer


# Create your views here.
class CategoriesViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all().order_by('-create_time')
    permission_classes = [IsAdminOrReadOnly]

    def get_serializer_class(self):
        if self.action == 'retrieve':
            return CategoriesDetailSerializer
        return CategoriesSerializer

    def create(self, request, *args, **kwargs):
        """
        新建分类
        """
        return super().create(request, *args, **kwargs)

    def list(self, request, *args, **kwargs):
        """
        获取分类列表
        """
        return super().list(request, *args, **kwargs)

    def retrieve(self, request, *args, **kwargs):
        """
        查看分类详情
        """
        return super().retrieve(request, *args, **kwargs)

    def update(self, request, *args, **kwargs):
        """
        更新分类
        """
        return super().update(request, *args, **kwargs)

    def partial_update(self, request, *args, **kwargs):
        """
        更新分类
        """
        return super().partial_update(request, *args, **kwargs)

    def destroy(self, request, *args, **kwargs):
        """
        删除分类
        """
        return super().destroy(request, *args, **kwargs)
