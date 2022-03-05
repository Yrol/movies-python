from core.common.view.base_views import BaseUpdateAPIView
from core.common.view.base_views import BaseRetrieveAPIView, BaseCreateAPIView
from core.models import Movies
from core.movies.serializers.movies_serializers import MoviesSerializer
from core.common.view.base_views import BaseListAPIView


class MoviesListView(BaseListAPIView):
    serializer_class = MoviesSerializer
    name = 'list-movies'
    def get_queryset(self):
        qs = Movies.objects.all().order_by('id')[::-1]
        return qs


class MoviesRetrieveView(BaseRetrieveAPIView):
    serializer_class = MoviesSerializer
    lookup_field = 'pk'
    name = 'retrive-movie'
    
    def get_queryset(self):
        """
        - self.kwargs.get -  will expose all the query paramters sent in teh URL (available inside get_queryset)
        - here we access the 'pk' as in its expected in the URL -> re_path(r'^genres/(?P<pk>[0-9]+)$'
        """
        id = self.kwargs.get(self.lookup_field, None)
        if id:
            return Movies.objects.filter(id=id)
        return None
    
    
class MovieCreateView(BaseCreateAPIView):
    queryset = Movies.objects.all()
    serializer_class = MoviesSerializer
    name = 'create-movie'


class MovieUpdateView(BaseUpdateAPIView):
    queryset = Movies.objects.all()
    serializer_class = MoviesSerializer
    name = 'update-movie'