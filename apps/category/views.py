from rest_framework import viewsets
from rest_framework import status
from drf_spectacular.utils import extend_schema
from .models import Category
from utils.drf_utils.custom_permissions import IsSuperuserOrReadOnly
from .serializers import CategoriesSerializer, CategoriesDetailSerializer
from utils.drf_utils.custom_json_response import enveloper, JsonResponse


# Create your views here.
@extend_schema(tags=['分类管理'])
class CategoriesViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all().order_by('-create_time')
    permission_classes = [IsSuperuserOrReadOnly]

    def get_serializer_class(self):
        if self.action == 'retrieve':
            return CategoriesDetailSerializer
        return CategoriesSerializer

    @extend_schema(responses=enveloper(CategoriesSerializer, False))
    def create(self, request, *args, **kwargs):
        """
        新建分类
        """
        res = super().create(request, *args, **kwargs)
        return JsonResponse(data=res.data, msg='success', code=20000, status=status.HTTP_201_CREATED,
                            headers=res.headers)

    @extend_schema(responses=enveloper(CategoriesSerializer, False))
    def list(self, request, *args, **kwargs):
        """
        获取分类列表
        """
        res = super().list(request, *args, **kwargs)
        return JsonResponse(data=res.data, msg='success', code=20000, status=status.HTTP_200_OK,
                            headers=res.headers)

    @extend_schema(responses=enveloper(CategoriesDetailSerializer, False))
    def retrieve(self, request, *args, **kwargs):
        """
        查看分类详情
        """
        res = super().retrieve(request, *args, **kwargs)
        return JsonResponse(data=res.data, msg='success', code=20000, status=status.HTTP_200_OK,
                            headers=res.headers)

    @extend_schema(responses=enveloper(CategoriesSerializer, False))
    def update(self, request, *args, **kwargs):
        """
        更新分类
        """
        res = super().update(request, *args, **kwargs)
        return JsonResponse(data=res.data, msg='success', code=20000, status=status.HTTP_200_OK,
                            headers=res.headers)

    @extend_schema(responses=enveloper(CategoriesSerializer, False))
    def partial_update(self, request, *args, **kwargs):
        """
        更新分类
        """
        res = super().partial_update(request, *args, **kwargs)
        return JsonResponse(data=res.data, msg='success', code=20000, status=status.HTTP_200_OK,
                            headers=res.headers)

    def destroy(self, request, *args, **kwargs):
        """
        删除分类
        """
        return super().destroy(request, *args, **kwargs)
