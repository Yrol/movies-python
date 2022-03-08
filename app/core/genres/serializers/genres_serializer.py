from core.common.serializers.base import BaseModelSerializer
from core.models import Genre
from django.db import transaction
from rest_framework import serializers
from rest_framework.exceptions import APIException


class GenresSerializer(BaseModelSerializer):
    id = serializers.IntegerField(read_only=False, required=False)
    class Meta:
        model = Genre
        fields = ('id', 'name', 'description',)
        
    def validate_name(self, value):
        if self.instance is None or self.instance.name != value:
            queryset = self.Meta.model.objects.filter(name=value)
            if queryset.exists() and (self.field_name is None):
                raise APIException("Genre with the name {} already exists.".format(value))
        return value
        
    @transaction.atomic
    def create(self, validated_data):
        instance = self.Meta.model.objects.create(**validated_data)
        return instance