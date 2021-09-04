from rest_framework import viewsets
from .models import Tag
from utils.drf_utils.custom_permissions import IsAdminOrReadOnly
from .serializers import TagsSerializer


# Create your views here.
class TagsViewSet(viewsets.ModelViewSet):
    queryset = Tag.objects.all().order_by('-create_time')
    permission_classes = [IsAdminOrReadOnly]
    serializer_class = TagsSerializer

    def create(self, request, *args, **kwargs):
        """
        新建标签
        """
        return super().create(request, *args, **kwargs)

    def list(self, request, *args, **kwargs):
        """
        获取标签列表
        """
        return super().list(request, *args, **kwargs)

    def retrieve(self, request, *args, **kwargs):
        """
        查看标签详情
        """
        return super().retrieve(request, *args, **kwargs)

    def update(self, request, *args, **kwargs):
        """
        更新标签
        """
        return super().update(request, *args, **kwargs)

    def partial_update(self, request, *args, **kwargs):
        """
        更新标签
        """
        return super().partial_update(request, *args, **kwargs)

    def destroy(self, request, *args, **kwargs):
        """
        删除标签
        """
        return super().destroy(request, *args, **kwargs)
