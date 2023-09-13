from rest_framework import serializers
from .models import Certificate, CertifyingInstitution, Project, Profile


class ProjectsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = [
            "id",
            "name",
            "description",
            "github_url",
            "keyword",
            "key_skill",
            "profile",
        ]


class ProfilesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = ["id", "name", "github", "linkedin", "bio"]


class CertificateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Certificate
        fields = [
            "id",
            "name",
            "timestamp",
            "certifying_institution",
            "profiles",
        ]


class NestedCertificateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Certificate
        fields = [
            "id",
            "name",
            "timestamp",
            "profiles",
        ]


class CertifyingInstitutionSerializer(serializers.ModelSerializer):
    certificates = NestedCertificateSerializer(many=True)

    class Meta:
        model = CertifyingInstitution
        fields = [
            "id",
            "name",
            "url",
            "certificates",
        ]

    def create(self, validated_data):
        certificates_data = validated_data.pop("certificates")
        certificates_data_without_certificates = (
            CertifyingInstitution.objects.create(**validated_data)
        )
        for certifying_institution in certificates_data:
            Certificate.objects.create(
                certifying_institution=certificates_data_without_certificates,
                **certifying_institution,
            )
        return certificates_data_without_certificates
