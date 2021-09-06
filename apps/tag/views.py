from rest_framework import viewsets
from rest_framework import status
from drf_spectacular.utils import extend_schema
from .models import Tag
from utils.drf_utils.custom_permissions import IsSuperuserOrReadOnly
from .serializers import TagsSerializer
from utils.drf_utils.custom_json_response import enveloper, JsonResponse


# Create your views here.
@extend_schema(tags=['标签管理'])
class TagsViewSet(viewsets.ModelViewSet):
    queryset = Tag.objects.all().order_by('-create_time')
    permission_classes = [IsSuperuserOrReadOnly]
    serializer_class = TagsSerializer

    @extend_schema(responses=enveloper(TagsSerializer, False))
    def create(self, request, *args, **kwargs):
        """
        新建标签
        """
        res = super().create(request, *args, **kwargs)
        return JsonResponse(data=res.data, msg='success', code=20000, status=status.HTTP_201_CREATED,
                            headers=res.headers)

    @extend_schema(responses=enveloper(TagsSerializer, True))
    def list(self, request, *args, **kwargs):
        """
        获取标签列表

        `响应体数据格式以下方示例为准`
        ```json
        # 当响应状态码为200时(response_code = 200)
        {
          "code": 20000,
          "message": "success",
          "data": {
            "count": 7,
            "next": "http://127.0.0.1:8000/api/tags/?page=2&size=1",
            "previous": null,
            "results": [
              {
                "id": 7,
                "create_time": "2021-09-06 04:02:46",
                "update_time": "2021-09-06 04:02:46",
                "name": "达芙妮副科级"
              }
            ],
            "total_pages": 7,
            "current_page": 1
          }
        }
        ```
        """
        res = super().list(request, *args, **kwargs)
        return JsonResponse(data=res.data, msg='success', code=20000, status=status.HTTP_200_OK,
                            headers=res.headers)

    @extend_schema(responses=enveloper(TagsSerializer, False))
    def retrieve(self, request, *args, **kwargs):
        """
        查看标签详情
        """
        res = super().retrieve(request, *args, **kwargs)
        return JsonResponse(data=res.data, msg='success', code=20000, status=status.HTTP_200_OK,
                            headers=res.headers)

    @extend_schema(responses=enveloper(TagsSerializer, False))
    def update(self, request, *args, **kwargs):
        """
        更新标签
        """
        res = super().update(request, *args, **kwargs)
        return JsonResponse(data=res.data, msg='success', code=20000, status=status.HTTP_200_OK,
                            headers=res.headers)

    @extend_schema(responses=enveloper(TagsSerializer, False))
    def partial_update(self, request, *args, **kwargs):
        """
        更新标签
        """
        res = super().partial_update(request, *args, **kwargs)
        return JsonResponse(data=res.data, msg='success', code=20000, status=status.HTTP_200_OK,
                            headers=res.headers)

    def destroy(self, request, *args, **kwargs):
        """
        删除标签
        """
        return super().destroy(request, *args, **kwargs)
