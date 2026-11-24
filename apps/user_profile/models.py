from django.db import models
from django.contrib.auth.models import User

# Add the 'role' field and helper properties directly to the User (auth_user table)
if not hasattr(User, "role"):
    User.add_to_class(
        "role",
        models.CharField(
            max_length=50,
            choices=[("Patient", "Patient"), ("Professional", "Professional")],
            default="Patient",
        ),
    )
if not hasattr(User, "is_patient"):
    User.add_to_class(
        "is_patient",
        property(lambda self: getattr(self, "role", "Patient") == "Patient"),
    )
if not hasattr(User, "is_professional"):
    User.add_to_class(
        "is_professional",
        property(lambda self: getattr(self, "role", "") == "Professional"),
    )


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(upload_to="profile/", blank=True, null=True)
    bio = models.TextField(blank=True)
    data_privacy_consent = models.BooleanField(default=False)

    class Meta:
        db_table = "user_profile"

    def __str__(self):
        return f"{self.user.username} ({self.role})"

    @property
    def role(self):
        return getattr(self.user, "role", "Patient")

    @role.setter
    def role(self, value):
        self.user.role = value
        if self.user.pk:
            self.user.save(update_fields=["role"])

    @property
    def designation(self):
        return self.role

    @designation.setter
    def designation(self, value):
        self.role = value

    @property
    def is_patient(self):
        return self.user.is_patient

    @property
    def is_doctor(self):
        prof = getattr(self.user, "professional", None)
        return self.is_professional and ("doctor" in getattr(prof, "specialty", "").lower() if prof else False)

    @property
    def is_therapist(self):
        prof = getattr(self.user, "professional", None)
        return self.is_professional and ("therapist" in getattr(prof, "specialty", "").lower() if prof else False)

    @property
    def is_professional(self):
        return self.user.is_professional



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
        full = f"{self.user.first_name} {self.user.last_name}".strip()
        display_name = full if full else self.user.username
        if self.specialty:
            return f"{display_name} ({self.specialty})"
        return f"Dr. {self.user.last_name}" if self.user.last_name else f"Professional: {display_name}"



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
