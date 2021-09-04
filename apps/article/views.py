from rest_framework import viewsets
from rest_framework.response import Response
from django_filters import rest_framework as filters
from .models import Article
from .serializers import ArticlesRetrieveDestroySerializer, ArticlesListSerializer, ArticlesCreateUpdateSerializer
from utils.drf_utils.custom_permissions import IsAdminOrReadOnly


class ArticleTitleFilter(filters.FilterSet):
    """
    自定义文章标题过滤器类，实现对文章标题进行模糊搜索(不区分大小写)
    """
    title = filters.CharFilter(field_name='title', lookup_expr='icontains', label='文章标题(模糊搜索且不区分大小写)')

    class Meta:
        model = Article
        fields = ['title', 'category']


# Create your views here.
class ArticlesViewSet(viewsets.ModelViewSet):
    queryset = Article.objects.all().order_by('-create_time')
    permission_classes = [IsAdminOrReadOnly]
    # 使用自定义文章标题过滤器类类
    filterset_class = ArticleTitleFilter

    def get_serializer_class(self):
        """
        根据不同的action选择不同的序列化器类
        """
        if self.action == 'list':
            return ArticlesListSerializer
        elif self.action == 'create' or self.action == 'update' or self.action == 'partial_update':
            return ArticlesCreateUpdateSerializer
        return ArticlesRetrieveDestroySerializer

    def create(self, request, *args, **kwargs):
        """
        新建文章
        """
        return super().create(request, *args, **kwargs)

    def list(self, request, *args, **kwargs):
        """
        获取文章列表
        """
        return super().list(request, *args, **kwargs)

    def retrieve(self, request, *args, **kwargs):
        """
        查看文章详情
        """
        instance = self.get_object()
        serializer = self.get_serializer(instance)
        if not request.user.is_superuser:
            # 如果当前请求的用户不是超级管理员则不返回body字段的原始markdown数据
            data = serializer.data
            data.pop('body')
            return Response(data)
        return Response(serializer.data)

    def update(self, request, *args, **kwargs):
        """
        更新文章
        """
        return super().update(request, *args, **kwargs)

    def partial_update(self, request, *args, **kwargs):
        """
        更新文章
        """
        return super().partial_update(request, *args, **kwargs)

    def destroy(self, request, *args, **kwargs):
        """
        删除文章
        """
        return super().destroy(request, *args, **kwargs)

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

    def perform_update(self, serializer):
        serializer.save(author=self.request.user)
