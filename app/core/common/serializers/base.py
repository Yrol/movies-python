from rest_framework import serializers
from rest_framework.exceptions import APIException
from rest_framework import status

class BaseModelSerializer(serializers.ModelSerializer):
    def get_current_user(self):
        request = self.context['request']
        if request and hasattr(request, 'user'):
            return request.user
        else:
            raise APIException('Couldn\'t find user', status=status.HTTP_400_BAD_REQUEST)