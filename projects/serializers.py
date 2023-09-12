from rest_framework import serializers
from .models import Project, Profile


class ProjectsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = (
            "id",
            "name",
            "description",
            "github_url",
            "keyword",
            "key_skill",
            "profile",
        )


class ProfilesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = ("id", "name", "github", "linkedin", "bio")
