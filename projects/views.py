from django.shortcuts import get_object_or_404, render
from rest_framework import viewsets
from rest_framework.permissions import AllowAny, IsAuthenticated
from .models import Certificate, CertifyingInstitution, Project, Profile
from .serializers import (
    CertificateSerializer,
    ProjectsSerializer,
    ProfilesSerializer,
    CertifyingInstitutionSerializer,
)


class ProjectsViewSet(viewsets.ModelViewSet):
    queryset = Project.objects.all()
    serializer_class = ProjectsSerializer


class ProfileViewSet(viewsets.ModelViewSet):
    queryset = Profile.objects.all()
    serializer_class = ProfilesSerializer

    def get_permissions(self):
        if self.request.method == "GET":
            return [AllowAny()]
        return [IsAuthenticated()]

    def retrieve(self, request, *args, **kwargs):
        if request.method == "GET":
            profile = get_object_or_404(Profile, pk=kwargs["pk"])
            certificates = Certificate.objects.filter(profiles=profile)
            projects = Project.objects.filter(profile=profile)
            return render(
                request,
                "profile_detail.html",
                {
                    "profile": profile,
                    "certificates": certificates,
                    "projects": projects,
                },
            )
        return super().retrieve(request, *args, **kwargs)


class CertificateViewSet(viewsets.ModelViewSet):
    queryset = Certificate.objects.all()
    serializer_class = CertificateSerializer

    # def perform_create(self, serializer):
    #     print(serializer)
    #     certificate_without_profiles = {**serializer.validated_data}
    #     del certificate_without_profiles["profiles"]
    #     new_certificate = Certificate(**certificate_without_profiles)
    #     new_certificate.save()
    #     for profile in serializer.validated_data["profiles"]:
    #         new_certificate.add_profile(profile)


class CertifyingInstitutionViewSet(viewsets.ModelViewSet):
    queryset = CertifyingInstitution.objects.all()
    serializer_class = CertifyingInstitutionSerializer
