from django.db import models
from moods.models import Mood  # Import the Mood model

class Food(models.Model):
    name = models.CharField(max_length=100)
    emoji = models.CharField(max_length=10, null=True, blank=True)
    mood = models.ForeignKey(Mood, on_delete=models.CASCADE, null=True, blank=True)  # Add this line

    def __str__(self):
        return f"{self.emoji or ''} {self.name}"
