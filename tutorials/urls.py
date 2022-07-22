
from django.contrib import admin
from django.urls import include, path
from django.contrib.auth.models import User
from rest_framework import routers
from quickstart import serializers, views

router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet)
router.register(r'groups', views.GroupViewSet)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
]
