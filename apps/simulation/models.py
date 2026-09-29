from django.db import models
from django.contrib.auth.models import User


class AscensionRecord(models.Model):
    # Links the data to the specific user account
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)

    # Enterprise Privacy Field
    anonymized_id = models.CharField(max_length=100, blank=True, null=True)

    # Simulation Data
    scenario = models.CharField(max_length=255)
    target_level = models.CharField(max_length=100)
    peak_hr = models.FloatField()
    end_hr = models.FloatField()
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        name = self.user.username if self.user else self.anonymized_id
        return f"{name} | {self.scenario} | Peak HR: {self.peak_hr}"
