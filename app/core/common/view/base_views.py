from rest_framework import mixins
from rest_framework import status
from rest_framework.response import Response


"""
BASE Mixins
"""

class BaseRetriveModelMixin(mixins.RetrieveModelMixin):
    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance, context={'request': request})
        return Response(serializer.data)
    
class BaseListModelMixin(mixins.ListModelMixin):
    """
    List a queryset.
    """
    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())

        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True, context={'request': request})
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(queryset, many=True, context={'request': request})
        return Response(serializer.data)

class BaseCreateModelMixin(mixins.CreateModelMixin):
        def create(self, request, *args, **kwargs):
            serializer = self.get_serializer(data=request.data, context={'request': request})
            serializer.is_valid(raise_exception=True)
            self.perform_create(serializer)
            headers = self.get_success_headers(serializer.data)
            return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)


"""
BASE API Classes
"""

class BaseRetrieveAPIView(BaseRetriveModelMixin):
    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

class BaseListAPIView(BaseListModelMixin):
    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

class BaseCreateAPIView(BaseCreateModelMixin):
    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)
    