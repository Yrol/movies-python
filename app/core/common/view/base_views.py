from rest_framework import mixins
from rest_framework import status
from rest_framework.response import Response
from rest_framework.generics import GenericAPIView

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

class BaseUpdateModelMixins(mixins.UpdateModelMixin):
        def update(self, request, *args, **kwargs):
            partial = kwargs.pop('partial', False)
            instance = self.get_object()
            serializer = self.get_serializer(instance, context={'request': request}, data=request.data, partial=partial)
            serializer.is_valid(raise_exception=True)
            self.perform_update(serializer)

            if getattr(instance, '_prefetched_objects_cache', None):
                # If 'prefetch_related' has been applied to a queryset, we need to
                # forcibly invalidate the prefetch cache on the instance.
                instance._prefetched_objects_cache = {}

            return Response(serializer.data)


"""
BASE API Classes
"""

class BaseAPIView(GenericAPIView):
    pass

class BaseRetrieveAPIView(BaseRetriveModelMixin, BaseAPIView):
    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

class BaseListAPIView(BaseListModelMixin, BaseAPIView):
    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

class BaseCreateAPIView(BaseCreateModelMixin, BaseAPIView):
    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)
    
class BaseUpdateAPIView(BaseUpdateModelMixins, BaseAPIView):
    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)
    
    def patch(self, request, *args, **kwargs):
        return self.partial_update(request, *args, **kwargs)
    