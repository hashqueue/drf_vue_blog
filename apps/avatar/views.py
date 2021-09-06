from rest_framework import viewsets
from rest_framework import status
from drf_spectacular.utils import extend_schema
from .models import Avatar
from utils.drf_utils.custom_permissions import IsSuperuserOrReadOnly
from .serializers import AvatarsSerializer
from utils.drf_utils.custom_json_response import enveloper, JsonResponse


# Create your views here.
@extend_schema(tags=['文章标题背景图管理'])
class AvatarsViewSet(viewsets.ModelViewSet):
    queryset = Avatar.objects.all().order_by('-create_time')
    permission_classes = [IsSuperuserOrReadOnly]
    serializer_class = AvatarsSerializer

    @extend_schema(responses=enveloper(AvatarsSerializer, False))
    def create(self, request, *args, **kwargs):
        """
        新建文章标题背景图
        """
        res = super().create(request, *args, **kwargs)
        return JsonResponse(data=res.data, msg='success', code=20000, status=status.HTTP_201_CREATED,
                            headers=res.headers)

    @extend_schema(responses=enveloper(AvatarsSerializer, True))
    def list(self, request, *args, **kwargs):
        """
        获取文章标题背景图列表

        `响应体数据格式以下方示例为准`
        ```json
        # 当响应状态码为200时(response_code = 200)
        {
          "code": 20000,
          "message": "success",
          "data": {
            "count": 2,
            "next": "http://127.0.0.1:8000/api/avatars/?page=2&size=1",
            "previous": null,
            "results": [
              {
                "id": 2,
                "create_time": "2021-09-07 00:39:38",
                "update_time": "2021-09-07 00:39:38",
                "url": "https://cdn.jsdelivr.net/gh/hashqueue/blog-image-hosting@master/wallpapers/20210605145946.jpg"
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

    @extend_schema(responses=enveloper(AvatarsSerializer, False))
    def retrieve(self, request, *args, **kwargs):
        """
        查看文章标题背景图详情
        """
        res = super().retrieve(request, *args, **kwargs)
        return JsonResponse(data=res.data, msg='success', code=20000)

    @extend_schema(responses=enveloper(AvatarsSerializer, False))
    def update(self, request, *args, **kwargs):
        """
        更新文章标题背景图
        """
        res = super().update(request, *args, **kwargs)
        return JsonResponse(data=res.data, msg='success', code=20000)

    @extend_schema(responses=enveloper(AvatarsSerializer, False))
    def partial_update(self, request, *args, **kwargs):
        """
        更新文章标题背景图
        """
        kwargs['partial'] = True
        return self.update(request, *args, **kwargs)

    def destroy(self, request, *args, **kwargs):
        """
        删除文章标题背景图
        """
        return super().destroy(request, *args, **kwargs)
