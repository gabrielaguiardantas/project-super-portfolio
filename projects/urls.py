from rest_framework import routers
from django.urls import path, include
from projects.views import (
    ProjectsViewSet,
    ProfileViewSet,
    CertificateViewSet,
    CertifyingInstitutionViewSet,
)


router = routers.DefaultRouter()
router.register(r"projects", ProjectsViewSet)
router.register(r"profiles", ProfileViewSet)
router.register(r"certificates", CertificateViewSet)
router.register(r"certifying-institutions", CertifyingInstitutionViewSet)


urlpatterns = [path("", include(router.urls))]
