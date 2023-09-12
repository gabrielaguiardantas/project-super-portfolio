from rest_framework import routers
from django.urls import path, include
from projects.views import ProjectsViewSet, ProfilesViewSet


router = routers.DefaultRouter()
router.register(r"projects", ProjectsViewSet)
router.register(r"profiles", ProfilesViewSet)


urlpatterns = [path("", include(router.urls))]
