"""w created serializers.py at 2021/9/3 下午12:12"""
from rest_framework import serializers
from utils.drf_utils.base_model_serializer import BaseModelSerializer
from .models import Category
from article.models import Article


class CategoriesSerializer(BaseModelSerializer):
    class Meta:
        model = Category
        fields = "__all__"


class ArticleCategoriesDetailSerializer(serializers.ModelSerializer):
    """给分类详情的嵌套序列化器"""
    url = serializers.HyperlinkedIdentityField(view_name='article-detail')

    class Meta:
        model = Article
        fields = ['url', 'title', ]


class CategoriesDetailSerializer(BaseModelSerializer):
    articles = ArticleCategoriesDetailSerializer(many=True, read_only=True, help_text='属于当前分类下的文章列表')

    class Meta:
        model = Category
        fields = "__all__"
