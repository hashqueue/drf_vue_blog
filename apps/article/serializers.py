"""w created serializers.py at 2021/9/3 下午12:12"""
from utils.drf_utils.base_model_serializer import BaseModelSerializer
from .models import Article
from user.serializers import UserSerializer


class ArticleSerializer(BaseModelSerializer):
    # 嵌套序列化器
    author = UserSerializer(read_only=True)

    class Meta:
        model = Article
        fields = "__all__"
        extra_kwargs = {
            'body': {
                'write_only': True
            }
        }


class ArticleDetailSerializer(BaseModelSerializer):
    author = UserSerializer(read_only=True)

    class Meta:
        model = Article
        fields = "__all__"
