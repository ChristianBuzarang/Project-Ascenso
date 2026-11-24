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
        ("Professional", "Professional (Doctor, Psychiatrist, Therapist, etc.)"),
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
        label="Role",
    )
    specialty = forms.CharField(
        max_length=100,
        required=False,
        label="Clinical Specialty (For Professionals)",
        widget=forms.TextInput(
            attrs={"placeholder": "e.g. Doctor, Psychiatrist, Clinical Psychologist, Therapist"}
        ),
    )
    license_number = forms.CharField(
        max_length=100,
        required=False,
        label="License Number (For Professionals)",
        widget=forms.TextInput(
            attrs={"placeholder": "e.g. MD-12345 or LIC-8800"}
        ),
    )

    field_order = [
        "username",
        "email",
        "first_name",
        "last_name",
        "designation",
        "specialty",
        "license_number",
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
            user = form.save(commit=False)
            role = form.cleaned_data.get("designation", "Patient")
            user.role = role
            user.save()
            form.save_m2m()

            specialty_input = form.cleaned_data.get("specialty", "").strip()
            license_input = form.cleaned_data.get("license_number", "").strip()

            # Initialize User Profile in Supabase
            Profile.objects.get_or_create(user=user)

            # Initialize specific role table in Supabase
            if role == "Patient":
                Patient.objects.get_or_create(user=user)
            elif role == "Professional":
                specialty = specialty_input if specialty_input else "Doctor / Psychiatrist"
                license_no = license_input if license_input else f"PRO-{user.id:04d}"
                Professional.objects.get_or_create(
                    user=user,
                    defaults={
                        "specialty": specialty,
                        "license_number": license_no,
                    },
                )


            # Initialize User Settings
            UserSettings.objects.get_or_create(user=user)

            login(request, user)
            return redirect("home:home")
    else:
        form = ExtendedRegistrationForm()
    return render(request, "register/register.html", {"form": form})
