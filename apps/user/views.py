import base64
from rest_framework import viewsets
from rest_framework import status
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from rest_framework_simplejwt.exceptions import InvalidToken, TokenError
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer, TokenRefreshSerializer
from drf_spectacular.utils import extend_schema
from django.contrib.auth.models import User
from utils.drf_utils.custom_permissions import IsSuperuserOrReadOnly
from .serializers import UsersSerializer
from utils.drf_utils.custom_json_response import enveloper, JsonResponse


# Create your views here.
@extend_schema(tags=['用户管理'])
class UsersViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all().order_by('-date_joined')
    permission_classes = [IsSuperuserOrReadOnly]
    serializer_class = UsersSerializer

    @extend_schema(responses=enveloper(UsersSerializer, False))
    def create(self, request, *args, **kwargs):
        """
        新建用户
        """
        res = super().create(request, *args, **kwargs)
        return JsonResponse(data=res.data, msg='success', code=20000, status=status.HTTP_201_CREATED,
                            headers=res.headers)

    @extend_schema(responses=enveloper(UsersSerializer, True))
    def list(self, request, *args, **kwargs):
        """
        获取用户列表

        `响应体数据格式以下方示例为准`
        ```json
        # 当响应状态码为200时(response_code = 200)
        {
          "code": 20000,
          "message": "success",
          "data": {
            "count": 1,
            "next": null,
            "previous": null,
            "results": [
              {
                "id": 1,
                "date_joined": "2021-09-03 04:25:25",
                "last_login": "2021-09-04T01:04:14.859169",
                "is_superuser": true,
                "username": "admin",
                "first_name": "",
                "last_name": "",
                "email": "1912315910@qq.com",
                "is_staff": true,
                "is_active": true,
                "groups": [],
                "user_permissions": []
              }
            ],
            "total_pages": 1,
            "current_page": 1
          }
        }
        ```
        """
        res = super().list(request, *args, **kwargs)
        return JsonResponse(data=res.data, msg='success', code=20000)

    @extend_schema(responses=enveloper(UsersSerializer, False))
    def retrieve(self, request, *args, **kwargs):
        """
        查看用户详情
        """
        res = super().retrieve(request, *args, **kwargs)
        return JsonResponse(data=res.data, msg='success', code=20000)

    @extend_schema(responses=enveloper(UsersSerializer, False))
    def update(self, request, *args, **kwargs):
        """
        更新用户
        """
        res = super().update(request, *args, **kwargs)
        return JsonResponse(data=res.data, msg='success', code=20000)

    @extend_schema(responses=enveloper(UsersSerializer, False))
    def partial_update(self, request, *args, **kwargs):
        """
        更新用户
        """
        kwargs['partial'] = True
        return self.update(request, *args, **kwargs)

    def destroy(self, request, *args, **kwargs):
        """
        删除用户
        """
        return super().destroy(request, *args, **kwargs)


@extend_schema(tags=['用户认证'])
class MyTokenObtainPairView(TokenObtainPairView):
    serializer_class = TokenObtainPairSerializer

    @extend_schema(
        responses={
            200: {
                "type": "object",
                "properties": {
                    "code": {"type": "integer"},
                    "message": {"type": "string"},
                    "data": {"type": "object",
                             "properties": {
                                 "refresh": {"type": "string"},
                                 "access": {"type": "string"}
                             }}
                },
                "example": {
                    "code": 20000,
                    "message": "登录成功",
                    "data": {
                        "refresh": "e.g. eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.xxx",
                        "access": "e.g. eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.xxx",
                    }
                },
            },
        },
    )
    def post(self, request, *args, **kwargs):
        """
        用户登录
        * `access`就是其他接口认证要使用的token值
        """
        res = super().post(request, *args, **kwargs)
        return JsonResponse(data=res.data, msg='登录成功', code=20000, status=status.HTTP_200_OK)


@extend_schema(tags=['用户认证'])
class MyTokenRefreshView(TokenRefreshView):
    serializer_class = TokenRefreshSerializer

    @extend_schema(
        responses={
            200: {
                "type": "object",
                "properties": {
                    "code": {"type": "integer"},
                    "message": {"type": "string"},
                    "data": {"type": "object",
                             "properties": {
                                 "refresh": {"type": "string"},
                                 "access": {"type": "string"}
                             }}
                },
                "example": {
                    "code": 20000,
                    "message": "success",
                    "data": {
                        "refresh": "e.g. eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.xxx",
                        "access": "e.g. eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.xxx",
                    }
                },
            },
        },
    )
    def post(self, request, *args, **kwargs):
        """
        刷新token
        * `access`就是其他接口认证要使用的token值
        """
        res = super().post(request, *args, **kwargs)
        return JsonResponse(data=res.data, msg='success', code=20000, status=status.HTTP_200_OK)
