"""w created serializers.py at 2021/9/3 下午12:12"""
from rest_framework import serializers
from drf_spectacular.utils import extend_schema_field, OpenApiTypes
from tag.models import Tag
from utils.drf_utils.base_model_serializer import BaseHyperlinkedModelSerializer, BaseModelSerializer
from .models import Article


class ArticlesRetrieveDestroySerializer(BaseHyperlinkedModelSerializer):
    author = serializers.CharField(source='author.username', help_text='作者')
    category_name = serializers.CharField(source='category.name', required=False, help_text='分类名称')
    tags = serializers.SlugRelatedField(queryset=Tag.objects.all(), many=True, required=False, slug_field='name',
                                        help_text='文章标签')
    # md渲染为HTML后的正文
    body_html = serializers.SerializerMethodField(help_text='markdown解析为HTML后的正文')
    # md渲染为HTML渲染后的目录(toc)
    toc_html = serializers.SerializerMethodField(help_text='markdown解析为HTML后的目录')

    class Meta:
        model = Article
        fields = "__all__"

    @extend_schema_field(OpenApiTypes.STR)
    def get_body_html(self, obj):
        """
        对应body_html字段
        SerializerMethodField
            - This is a read-only field. It gets its value by calling a method on the serializer class it is attached to
                It can be used to add any sort of data to the serialized representation of your object.
            - Signature: SerializerMethodField(method_name=None)
            - method_name - The name of the method on the serializer to be called.
                If not included this defaults to get_<field_name>.
        """
        return obj.get_md()[0]

    @extend_schema_field(OpenApiTypes.STR)
    def get_toc_html(self, obj):
        """
        对应toc_html字段
        """
        return obj.get_md()[1]


class ArticlesListSerializer(BaseHyperlinkedModelSerializer):
    """
    article list
    """
    # 嵌套序列化器
    author = serializers.CharField(source='author.username', help_text='作者')
    category_name = serializers.CharField(source='category.name', required=False, help_text='分类名称')
    tags = serializers.SlugRelatedField(queryset=Tag.objects.all(), many=True, required=False, slug_field='name',
                                        help_text='文章标签')

    class Meta:
        model = Article
        exclude = ('body',)


class ArticlesCreateUpdateSerializer(BaseModelSerializer):
    """
    article create update partial_update
    """
    tags = serializers.SlugRelatedField(queryset=Tag.objects.all(), many=True, required=False, slug_field='name',
                                        help_text='文章标签')

    class Meta:
        model = Article
        exclude = ('author',)
        extra_kwargs = {
            'body': {
                'write_only': True
            }
        }

    def to_internal_value(self, data):
        """
        to_internal_value() 方法原本作用是将请求中的原始 Json 数据转化为 Python 表示形式（期间还会对字段有效性做初步检查）。
        它的执行时间比默认验证器的字段检查更早，因此有机会在此方法中将需要的数据创建好，
        然后等待检查的降临。isinstance() 确定标签数据是列表，才会循环并创建新数据。
        """
        tags_data = data.get('tags')
        if isinstance(tags_data, list):
            for tag_data in tags_data:
                if not Tag.objects.filter(name=tag_data).exists():
                    # 如果要创建的标签不存在，就创建它
                    Tag.objects.create(name=tag_data)
        return super().to_internal_value(data)
