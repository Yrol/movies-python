from core.common.view.base_views import BaseCreateAPIView, BaseListAPIView, BaseUpdateAPIView, BaseRetrieveAPIView
from core.genres.serializers.genres_serializer import GenresSerializer
from core.models import Genre


class GenreCreateView(BaseCreateAPIView):
    queryset = Genre.objects.all()
    serializer_class = GenresSerializer
    name = 'create-genre'
    
    
class GenreUpdateView(BaseUpdateAPIView):
    queryset = Genre.objects.all()
    serializer_class = GenresSerializer
    name = 'update-genre'
    
    
class GenreListView(BaseListAPIView):
    serializer_class = GenresSerializer
    name = 'list-genre'
    def get_queryset(self):
        qs = Genre.objects.all().order_by('id')[::-1]
        return qs

class GenreRetrieveView(BaseRetrieveAPIView):
    serializer_class = GenresSerializer
    lookup_field = 'pk'
    name = 'retrive-genre'
    
    def get_queryset(self):
        """
        - self.kwargs.get -  will expose all the query paramters sent in teh URL (available inside get_queryset)
        - here we access the 'pk' as in its expected in the URL -> re_path(r'^genres/(?P<pk>[0-9]+)$'
        """
        id = self.kwargs.get(self.lookup_field, None)
        if id:
            return Genre.objects.filter(id=id)
        return None
    