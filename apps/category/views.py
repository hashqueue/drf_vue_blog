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

    @extend_schema(responses=enveloper(CategoriesSerializer, True))
    def list(self, request, *args, **kwargs):
        """
        获取分类列表

        `响应体数据格式以下方示例为准`
        ```json
        # 当响应状态码为200时(response_code = 200)
        {
          "code": 20000,
          "message": "success",
          "data": {
            "count": 2,
            "next": "http://127.0.0.1:8000/api/categories/?page=2&size=1",
            "previous": null,
            "results": [
              {
                "id": 2,
                "create_time": "2021-09-04 16:16:27",
                "update_time": "2021-09-04 16:17:24",
                "name": "FastAPI"
              }
            ],
            "total_pages": 2,
            "current_page": 1
          }
        }
        ```
        """
        res = super().list(request, *args, **kwargs)
        return JsonResponse(data=res.data, msg='success', code=20000)

    @extend_schema(responses=enveloper(CategoriesDetailSerializer, False))
    def retrieve(self, request, *args, **kwargs):
        """
        查看分类详情
        """
        res = super().retrieve(request, *args, **kwargs)
        return JsonResponse(data=res.data, msg='success', code=20000)

    @extend_schema(responses=enveloper(CategoriesSerializer, False))
    def update(self, request, *args, **kwargs):
        """
        更新分类
        """
        res = super().update(request, *args, **kwargs)
        return JsonResponse(data=res.data, msg='success', code=20000)

    @extend_schema(responses=enveloper(CategoriesSerializer, False))
    def partial_update(self, request, *args, **kwargs):
        """
        更新分类
        """
        kwargs['partial'] = True
        return self.update(request, *args, **kwargs)

    def destroy(self, request, *args, **kwargs):
        """
        删除分类
        """
        return super().destroy(request, *args, **kwargs)
