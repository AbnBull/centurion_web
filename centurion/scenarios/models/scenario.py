from django.db import models
from django.utils import timezone
import datetime

# helper function for todays date callable
def default_midnight_today():
    today = timezone.now().date()
    return timezone.make_aware(datetime.datetime.combine(today, datetime.time.min))

class Scenario(models.Model):
    name = models.CharField(max_length=100, default="Unnamed Scenario")
    created_at = models.DateTimeField(auto_now_add=True)
    exercise_start_datetime = models.DateTimeField(blank=False, null=False, default=default_midnight_today)
    
    class Meta:
        ordering = ["-created_at"]

    def __str__(self):
        return self.name