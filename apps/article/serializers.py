"""w created serializers.py at 2021/9/3 下午12:12"""
from utils.drf_utils.base_model_serializer import BaseModelSerializer
from .models import Article


class ArticleSerializer(BaseModelSerializer):
    class Meta:
        model = Article
        fields = ("id", "title", "create_time", "update_time")


class ArticleDetailSerializer(BaseModelSerializer):
    class Meta:
        model = Article
        fields = "__all__"
