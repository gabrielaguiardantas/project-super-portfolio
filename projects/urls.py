from rest_framework import routers
from django.urls import path, include
from projects.views import ProjectsViewSet, ProfileViewSet


router = routers.DefaultRouter()
router.register(r"projects", ProjectsViewSet)
router.register(r"profiles", ProfileViewSet)


urlpatterns = [path("", include(router.urls))]
