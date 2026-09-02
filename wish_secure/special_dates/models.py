from django.db import models
from datetime import date
# Create your models here.
from django.contrib.auth.models import User


class SpecialDate(models.Model):

    DATE_TYPES = (
        ("Birthday", "Birthday"),
        ("Anniversary", "Anniversary"),
        ("First Date", "First Date"),
        ("First Meeting", "First Meeting"),
        ("Trip", "Trip"),
        ("Achievement", "Achievement"),
        ("Other", "Other"),
    )

    title = models.CharField(
        max_length=200
    )

    description = models.TextField(
        blank=True
    )

    date = models.DateField()

    date_type = models.CharField(
        max_length=30,
        choices=DATE_TYPES,
        default="Other"
    )

    icon = models.CharField(
        max_length=50,
        default="❤️"
    )

    repeat_yearly = models.BooleanField(
        default=True
    )

    created_by = models.ForeignKey(
        User,
        on_delete=models.CASCADE
    )

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    updated_at = models.DateTimeField(
        auto_now=True
    )

    def __str__(self):

        return self.title
    
    def next_occurrence(self):
    
        today = date.today()

        if not self.repeat_yearly:

            return self.date

        try:

            occurrence = self.date.replace(
                year=today.year
            )

        except ValueError:

            # Handles February 29
            occurrence = self.date.replace(
                year=today.year,
                day=28
            )

        if occurrence < today:

            try:

                occurrence = self.date.replace(
                    year=today.year + 1
                )

            except ValueError:

                occurrence = self.date.replace(
                    year=today.year + 1,
                    day=28
                )

        return occurrence


    def days_until(self):

        today = date.today()

        next_date = self.next_occurrence()

        return (next_date - today).days


    def is_today(self):

        return self.days_until() == 0