from django.db import models

from projects.validators import validate_fields


class Project(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField(max_length=500)
    github_url = models.URLField(blank=True)
    keyword = models.CharField(max_length=50)
    key_skill = models.CharField(max_length=50)
    profile = models.ForeignKey(
        "Profile",
        related_name="project",
        on_delete=models.CASCADE,
        null=True,
    )

    def __str__(self):
        return self.name


class Profile(models.Model):
    name = models.CharField(max_length=100)
    github = models.URLField(blank=True)
    linkedin = models.URLField(blank=True)
    bio = models.TextField()

    def __str__(self):
        return self.name


class CertifyingInstitution(models.Model):
    name = models.CharField(max_length=100, validators=[validate_fields])
    url = models.URLField(validators=[validate_fields])

    def __str__(self):
        return self.name


class Certificate(models.Model):
    name = models.CharField(max_length=100, validators=[validate_fields])
    timestamp = models.DateTimeField(
        auto_now_add=True, validators=[validate_fields]
    )
    certifying_institution = models.ForeignKey(
        "CertifyingInstitution",
        related_name="certificates",
        on_delete=models.CASCADE,
    )
    profiles = models.ManyToManyField(
        "Profile", related_name="certificates", blank=True
    )

    def add_profile(self, profile):
        self.profiles.add(profile)
        self.save()

    def remove_profile(self, profile):
        self.profiles.remove(profile)
        self.save()

    def __str__(self):
        return self.name
