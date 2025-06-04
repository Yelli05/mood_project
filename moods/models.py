from django.db import models

class Mood(models.Model):
    name = models.CharField(max_length=50)
    emoji = models.CharField(max_length=10, blank=True)

    def __str__(self):
        return f"{self.name} {self.emoji}"
