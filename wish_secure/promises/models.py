from django.db import models
from django.contrib.auth.models import User


class Promise(models.Model):

    STATUS_CHOICES = (
        ("Active", "Active"),
        ("Kept", "Kept"),
        ("Broken", "Broken"),
    )

    title = models.CharField(max_length=200)

    description = models.TextField()

    made_by = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="promises_made"
    )

    promise_date = models.DateField()

    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default="Active"
    )

    kept_at = models.DateTimeField(
        null=True,
        blank=True
    )

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    updated_at = models.DateTimeField(
        auto_now=True
    )

    def __str__(self):
        return self.title