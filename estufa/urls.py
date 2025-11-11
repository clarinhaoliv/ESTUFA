from django.contrib import admin
from django.urls import include, path
from .views import LeituraViewSet, AlertaViewSet
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'leituras', LeituraViewSet, basename='leituras')
router.register(r'alertas', AlertaViewSet, basename='alertas')

urlpatterns = [
    path('', include(router.urls)),
]
