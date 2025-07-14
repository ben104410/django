from django.db import models
from django.contrib.auth.models import User

class Attendance(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    check_in = models.DateTimeField()
    check_out = models.DateTimeField(blank=True, null=True)
    status = models.CharField(max_length=20, blank=True, null=True)  # optional

    def __str__(self):
        return f"{self.user.username} - {self.check_in.date()}"
