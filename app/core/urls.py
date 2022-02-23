from django.conf.urls import include
from django.contrib import admin
from django.urls import path
from rest_framework import routers


router = routers.SimpleRouter()

urlpatterns = [
    path('', include(router.urls))
]

