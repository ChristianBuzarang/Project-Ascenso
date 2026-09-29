from django.contrib import admin
from .models import Profile, Patient, Professional, ProfessionalAssignment

admin.site.register(Profile)
admin.site.register(Patient)
admin.site.register(Professional)


@admin.register(ProfessionalAssignment)
class ProfessionalAssignmentAdmin(admin.ModelAdmin):
    list_display = ("professional", "patient", "status", "assigned_date")
