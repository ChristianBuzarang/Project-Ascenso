from django.db import models
from django.contrib.auth.models import User


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(upload_to="profile/", blank=True, null=True)
    bio = models.TextField(blank=True)
    data_privacy_consent = models.BooleanField(default=False)

    class Meta:
        db_table = "user_profile"

    def __str__(self):
        return self.user.username


class Patient(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    class Meta:
        db_table = "patient"

    def __str__(self):
        return f"Patient: {self.user.username}"


class Professional(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    license_number = models.CharField(max_length=100)
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
