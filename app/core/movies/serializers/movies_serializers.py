from core.models import Genre
from core.genres.serializers.genres_serializer import GenresSerializer
from core.common.serializers.base import BaseModelSerializer
from core.models import Movies
from django.forms import ValidationError
from django.db import transaction
from drf_writable_nested import WritableNestedModelSerializer
from rest_framework.exceptions import APIException


class MoviesSerializer(BaseModelSerializer, WritableNestedModelSerializer):
    genre = GenresSerializer(required=False, allow_null=True)
    
    class Meta:
        model = Movies
        fields = ('name', 'genre', 'description',)
        
    def validate_name(self, value):
        if self.instance is None or self.instance.name != value:
            queryset = self.Meta.model.objects.filter(name=value)
            if queryset.exists() and (self.field_name is None):
                raise APIException("Movie with the name {} already exists.".format(value))
        return value
        
    @transaction.atomic
    def create(self, validated_data):
        
        genre = validated_data.pop('genre', None)
        
        if not genre:
            raise ValidationError('Genre is required')
        
        # already required in the model
        # if not genre['name']:
        #     raise ValidationError('Invalid Genre')
        try:
            current_genre = Genre.objects.get(name__iexact=genre['name'])
        except(Genre.DoesNotExist):
            raise ValidationError('Invalid Genre')
        
        instance = self.Meta.model.objects.create(genre = current_genre, **validated_data)
        return instance