from django.conf.urls import include
from django.urls import path, re_path
from rest_framework import routers

from core.genres.views import GenreCreateView, GenreListView, GenreUpdateView, GenreRetrieveView

router = routers.SimpleRouter()

urlpatterns = [
    path('', include(router.urls)),
    re_path(r'^genre/$', GenreCreateView.as_view(), name=GenreCreateView.name),
    re_path(r'^genre/(?P<pk>[0-9]+)$', GenreUpdateView.as_view(), name=GenreUpdateView.name),
    re_path(r'^genres/$', GenreListView.as_view(), name=GenreListView.name),
    re_path(r'^genres/(?P<pk>[0-9]+)$', GenreRetrieveView.as_view(), name=GenreRetrieveView.name),
]

