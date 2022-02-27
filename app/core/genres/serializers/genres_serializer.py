from core.common.serializers.base import BaseModelSerializer
from core.models import Genre
from django.db import transaction


class GenresSerializer(BaseModelSerializer):
    class Meta:
        model = Genre
        fields = ('name', 'description',)
        
    @transaction.atomic
    def create(self, validated_data):
        instance = self.Meta.model.objects.create(**validated_data)
        return instance