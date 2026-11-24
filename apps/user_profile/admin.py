from django.contrib import admin
from django.contrib.auth.models import User
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from unfold.admin import ModelAdmin
from .models import Profile, Patient, Professional, ProfessionalAssignment

# Re-register User in admin to surface the 'role' field
if admin.site.is_registered(User):
    admin.site.unregister(User)


@admin.register(User)
class UserWithRoleAdmin(ModelAdmin, BaseUserAdmin):
    list_display = ("username", "email", "first_name", "last_name", "role", "is_staff")
    list_filter = ("role", "is_staff", "is_superuser", "is_active")
    search_fields = ("username", "first_name", "last_name", "email")
    fieldsets = BaseUserAdmin.fieldsets + (
        ("System Role", {"fields": ("role",)}),
    )


@admin.register(Profile)
class ProfileAdmin(ModelAdmin):
    list_display = ("user", "get_role", "data_privacy_consent")
    list_filter = ("user__role", "data_privacy_consent")
    search_fields = (
        "user__username",
        "user__first_name",
        "user__last_name",
        "user__email",
    )

    @admin.display(description="Role (User Table)")
    def get_role(self, obj):
        return obj.user.role


@admin.register(Patient)
class PatientAdmin(ModelAdmin):
    list_display = ("id", "user", "get_email", "get_role")
    search_fields = (
        "user__username",
        "user__first_name",
        "user__last_name",
        "user__email",
    )

    @admin.display(description="Email")
    def get_email(self, obj):
        return obj.user.email

    @admin.display(description="Role")
    def get_role(self, obj):
        return obj.user.role



@admin.register(Professional)
class ProfessionalAdmin(ModelAdmin):
    list_display = ("id", "user", "specialty", "license_number")
    list_filter = ("specialty",)
    search_fields = (
        "user__username",
        "user__first_name",
        "user__last_name",
        "user__email",
        "license_number",
        "specialty",
    )


@admin.register(ProfessionalAssignment)
class ProfessionalAssignmentAdmin(ModelAdmin):
    list_display = ("id", "professional", "patient", "status", "assigned_date")
    list_filter = ("status", "assigned_date")
    search_fields = (
        "professional__user__username",
        "professional__user__last_name",
        "patient__user__username",
        "status",
    )

