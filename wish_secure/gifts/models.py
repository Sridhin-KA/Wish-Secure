from django.db import models
from django.contrib.auth.models import User


class Gift(models.Model):

    STATUS_CHOICES = (
        ("Idea", "Idea"),
        ("Planned", "Planned"),
        ("Bought", "Bought"),
        ("Given", "Given"),
    )

    title = models.CharField(max_length=200)

    description = models.TextField(
        blank=True
    )

    for_person = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="gifts_received"
    )

    added_by = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="gifts_added"
    )

    gift_date = models.DateField(
        null=True,
        blank=True
    )

    price = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        null=True,
        blank=True
    )

    link = models.URLField(
        blank=True
    )

    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default="Idea"
    )

    image = models.ImageField(
        upload_to="gifts/",
        blank=True,
        null=True
    )

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    updated_at = models.DateTimeField(
        auto_now=True
    )

    def __str__(self):
        return self.title