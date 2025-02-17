from django.db import models
from django.contrib.auth.models import User

class Message(models.Model):
    message = models.TextField()
    username = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField()
    room = models.CharField(max_length=20)
    
    class Meta:
        ordering = ["-created_at"]

    def __str__(self):
        return self.username + ' said ' + self.message