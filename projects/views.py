from rest_framework import viewsets
from .models import Project, Profile
from .serializers import ProjectsSerializer, ProfilesSerializer

# from .permissions import IsOwner


class ProjectsViewSet(viewsets.ModelViewSet):
    queryset = Project.objects.all()
    serializer_class = ProjectsSerializer
    # permission_classes = [IsOwner]

    def perform_create(self, serializer):
        serializer.save()


class ProfilesViewSet(viewsets.ModelViewSet):
    queryset = Profile.objects.all()
    serializer_class = ProfilesSerializer
    # permission_classes = [IsOwner]

    def perform_create(self, serializer):
        serializer.save()
