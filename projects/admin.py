from django.contrib import admin
from .models import Certificate, Profile, Project, CertifyingInstitution

# Register your models here.
admin.site.register(Project)
admin.site.register(Profile)


class CertificateInline(admin.StackedInline):
    model = Certificate


class CertifyingInstitutionAdmin(admin.ModelAdmin):
    inlines = [CertificateInline]


admin.site.register(CertifyingInstitution, CertifyingInstitutionAdmin)
admin.site.register(Certificate)
