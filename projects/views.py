from django.shortcuts import get_object_or_404, render
from rest_framework import viewsets
from rest_framework.permissions import AllowAny, IsAuthenticated
from .models import Project, Profile
from .serializers import ProjectsSerializer, ProfilesSerializer

# from .permissions import IsOwner


class ProjectsViewSet(viewsets.ModelViewSet):
    queryset = Project.objects.all()
    serializer_class = ProjectsSerializer
    # permission_classes = [IsOwner]

    def perform_create(self, serializer):
        serializer.save()


class ProfileViewSet(viewsets.ModelViewSet):
    queryset = Profile.objects.all()
    serializer_class = ProfilesSerializer
    # permission_classes = [IsOwner]

    def get_permissions(self):
        if self.request.method == "GET":
            return [AllowAny()]
        return [IsAuthenticated()]

    def retrieve(self, request, *args, **kwargs):
        if request.method == "GET":
            profile = get_object_or_404(Profile, pk=kwargs["pk"])
            return render(request, "profile_detail.html", {"profile": profile})
        return super().retrieve(request, *args, **kwargs)

    def perform_create(self, serializer):
        serializer.save()
