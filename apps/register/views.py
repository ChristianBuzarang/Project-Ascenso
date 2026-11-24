from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib.auth import login
from django.shortcuts import render, redirect
from django import forms
from apps.user_profile.models import Profile, Patient, Professional
from apps.user_settings.models import UserSettings


class ExtendedRegistrationForm(UserCreationForm):
    ROLE_CHOICES = [
        ("Patient", "Patient"),
        ("Doctor", "Doctor"),
        ("Therapist", "Therapist"),
    ]

    first_name = forms.CharField(
        max_length=30, required=True, label="First Name"
    )
    last_name = forms.CharField(
        max_length=30, required=True, label="Last Name"
    )
    email = forms.EmailField(
        max_length=254, required=True, label="Email"
    )
    designation = forms.ChoiceField(
        choices=ROLE_CHOICES,
        initial="Patient",
        required=True,
        label="Designation (Role)",
    )

    field_order = [
        "username",
        "email",
        "first_name",
        "last_name",
        "designation",
        "password1",
        "password2",
    ]

    class Meta(UserCreationForm.Meta):
        model = User
        fields = ("username", "email", "first_name", "last_name")


def register_view(request):
    if request.user.is_authenticated:
        return redirect("home:home")

    if request.method == "POST":
        form = ExtendedRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            role = form.cleaned_data.get("designation", "Patient")

            # Initialize User Profile with chosen role & designation in Supabase
            profile, created = Profile.objects.get_or_create(user=user)
            profile.role = role
            profile.designation = role
            profile.save()

            # Initialize specific role table in Supabase
            if role == "Patient":
                Patient.objects.get_or_create(user=user)
            elif role in ("Doctor", "Therapist"):
                Professional.objects.get_or_create(
                    user=user,
                    defaults={
                        "specialty": role,
                        "license_number": f"{role[:3].upper()}-{user.id:04d}",
                    },
                )

            # Initialize User Settings
            UserSettings.objects.get_or_create(user=user)

            login(request, user)
            return redirect("home:home")
    else:
        form = ExtendedRegistrationForm()
    return render(request, "register/register.html", {"form": form})
