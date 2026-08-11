from django.db import models
from django.contrib.auth.models import User


class Category(models.Model):

    name = models.CharField(max_length=100)

    icon = models.CharField(
        max_length=50,
        blank=True,
        null=True
    )

    def __str__(self):
        return self.name


class Wish(models.Model):

    PRIORITY = (
        ('High', 'High'),
        ('Medium', 'Medium'),
        ('Low', 'Low'),
    )

    STATUS = (
        ('Pending', 'Pending'),
        ('In Progress', 'In Progress'),
        ('Completed', 'Completed'),
    )

    VISIBILITY = (
        ('Shared', 'Shared'),
        ('Private', 'Private'),
    )

    title = models.CharField(max_length=200)

    description = models.TextField()

    category = models.ForeignKey(
        Category,
        on_delete=models.CASCADE
    )

    priority = models.CharField(
        max_length=20,
        choices=PRIORITY,
        default='Medium'
    )

    status = models.CharField(
        max_length=20,
        choices=STATUS,
        default='Pending'
    )

    visibility = models.CharField(
        max_length=20,
        choices=VISIBILITY,
        default='Shared'
    )

    created_by = models.ForeignKey(
        User,
        on_delete=models.CASCADE
    )

    image = models.ImageField(
        upload_to='wishes/',
        blank=True,
        null=True
    )
    completed_by = models.ForeignKey(
    User,
    on_delete=models.SET_NULL,
    null=True,
    blank=True,
    related_name="completed_wishes"
)

    completed_at = models.DateTimeField(
        null=True,
        blank=True
    )

    created_at = models.DateTimeField(auto_now_add=True)

    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title


class WishComment(models.Model):

    wish = models.ForeignKey(
        Wish,
        on_delete=models.CASCADE,
        related_name="comments"
    )

    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE
    )

    comment = models.TextField()

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} - {self.wish.title}"
    
class Activity(models.Model):

    ACTION_CHOICES = (
        ('added', 'Added'),
        ('commented', 'Commented'),
        ('completed', 'Completed'),
        ('edited', 'Edited'),
    )

    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE
    )

    wish = models.ForeignKey(
        Wish,
        on_delete=models.CASCADE,
        related_name='activities'
    )

    action = models.CharField(
        max_length=20,
        choices=ACTION_CHOICES
    )

    message = models.CharField(
        max_length=255,
        blank=True
    )

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    is_read = models.BooleanField(
        default=False
    )

    def __str__(self):

        return f"{self.user.username} - {self.action}"