from django.db import models
from django.contrib.auth.models import User


class UserDevice(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    device_name = models.CharField(max_length=100)
    mac_address = models.CharField(max_length=100)
    is_active = models.BooleanField(default=True)

    class Meta:
        db_table = "user_device"

    def __str__(self):
        return f"{self.device_name} ({self.user.username})"


class FearScenario(models.Model):
    created_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    category = models.CharField(max_length=50)
    name = models.CharField(max_length=150)
    description = models.TextField()
    media_file = models.CharField(max_length=255)
    is_active = models.BooleanField(default=True)

    class Meta:
        db_table = "fear_scenario"

    def __str__(self):
        return f"[{self.category}] {self.name}"


class AscensionRecord(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    scenario = models.ForeignKey(FearScenario, on_delete=models.SET_NULL, null=True)
    target_level = models.CharField(max_length=100)
    peak_hr = models.FloatField()
    end_hr = models.FloatField()

    # Clinical & Data Storage Fields
    patient_journal = models.TextField(blank=True, null=True)
    professional_notes = models.TextField(blank=True, null=True)
    ai_intervention_script = models.TextField(blank=True, null=True)
    report_pdf_url = models.CharField(max_length=255, blank=True, null=True)
    raw_biometric_url = models.CharField(max_length=255, blank=True, null=True)
    timestamp = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = "ascension_record"

    def __str__(self):
        username = self.user.username if self.user else "Anonymous"
        scenario_name = self.scenario.name if self.scenario else "Unknown Scenario"
        return f"{username} | {scenario_name} | {self.timestamp.strftime('%Y-%m-%d')}"
