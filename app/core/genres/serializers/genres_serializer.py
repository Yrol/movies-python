from core.common.serializers.base import BaseModelSerializer
from core.models import Genre
from django.db import transaction
from rest_framework import serializers


class GenresSerializer(BaseModelSerializer):
    id = serializers.IntegerField(read_only=False, required=False)
    class Meta:
        model = Genre
        fields = ('id', 'name', 'description',)
        
    @transaction.atomic
    def create(self, validated_data):
        instance = self.Meta.model.objects.create(**validated_data)
        return instance