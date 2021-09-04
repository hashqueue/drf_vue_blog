"""w created serializers.py at 2021/9/3 下午12:12"""
from utils.drf_utils.base_model_serializer import BaseModelSerializer
from .models import Tag


class TagsSerializer(BaseModelSerializer):
    class Meta:
        model = Tag
        fields = "__all__"

    def create(self, validated_data):
        tag_name = validated_data.get('name')
        if not Tag.objects.filter(name=tag_name).exists():
            # 只有要创建的标签不存在，才会在此时去创建
            return super().create(validated_data)

    def update(self, instance, validated_data):
        tag_name = validated_data.get('name')
        if not Tag.objects.filter(name=tag_name).exists():
            return super().update(instance, validated_data)
