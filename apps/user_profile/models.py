from django.db import models
from django.contrib.auth.models import User


class Profile(models.Model):
    ROLE_CHOICES = [
        ("Patient", "Patient"),
        ("Doctor", "Doctor"),
        ("Therapist", "Therapist"),
    ]
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    role = models.CharField(max_length=50, choices=ROLE_CHOICES, default="Patient")
    designation = models.CharField(
        max_length=100, choices=ROLE_CHOICES, default="Patient", blank=True
    )
    image = models.ImageField(upload_to="profile/", blank=True, null=True)
    bio = models.TextField(blank=True)
    data_privacy_consent = models.BooleanField(default=False)

    class Meta:
        db_table = "user_profile"

    def __str__(self):
        return f"{self.user.username} ({self.designation})"

    @property
    def is_patient(self):
        return self.designation == "Patient" or self.role == "Patient"

    @property
    def is_doctor(self):
        return self.designation == "Doctor" or self.role == "Doctor"

    @property
    def is_therapist(self):
        return self.designation == "Therapist" or self.role == "Therapist"

    @property
    def is_professional(self):
        return self.is_doctor or self.is_therapist

    @property
    def full_name(self):
        full = f"{self.user.first_name} {self.user.last_name}".strip()
        return full if full else self.user.username

    @property
    def profile_image(self):
        return self.image

    @profile_image.setter
    def profile_image(self, value):
        self.image = value


class Patient(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    class Meta:
        db_table = "patient"

    def __str__(self):
        return f"Patient: {self.user.username}"


class Professional(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    license_number = models.CharField(max_length=100, blank=True, default="")
    specialty = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        db_table = "professional"

    def __str__(self):
        return f"Dr. {self.user.last_name}"


class ProfessionalAssignment(models.Model):
    professional = models.ForeignKey(
        Professional, on_delete=models.CASCADE, related_name="patients"
    )
    patient = models.ForeignKey(
        Patient, on_delete=models.CASCADE, related_name="doctors"
    )
    assigned_date = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=50, default="Active")

    class Meta:
        db_table = "professional_assignment"

    def __str__(self):
        return f"Dr. {self.professional.user.last_name} -> {self.patient.user.username}"
