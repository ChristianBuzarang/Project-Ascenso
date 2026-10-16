from django.contrib import admin
from unfold.admin import ModelAdmin
from .models import Profile, Patient, Professional, ProfessionalAssignment


@admin.register(Profile)
class ProfileAdmin(ModelAdmin):
    pass


@admin.register(Patient)
class PatientAdmin(ModelAdmin):
    pass


@admin.register(Professional)
class ProfessionalAdmin(ModelAdmin):
    pass


@admin.register(ProfessionalAssignment)
class ProfessionalAssignmentAdmin(ModelAdmin):
    list_display = ("professional", "patient", "status", "assigned_date")
