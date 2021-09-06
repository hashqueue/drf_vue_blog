"""w created serializers.py at 2021/9/3 下午12:12"""
from utils.drf_utils.base_model_serializer import BaseModelSerializer
from .models import Avatar


class AvatarsSerializer(BaseModelSerializer):
    class Meta:
        model = Avatar
        fields = "__all__"
