from django.db import models

# from django.contrib.auth.models import User


# Create your models here.
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
