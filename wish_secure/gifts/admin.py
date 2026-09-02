from django.contrib import admin
from .models import Gift


@admin.register(Gift)
class GiftAdmin(admin.ModelAdmin):

    list_display = (
        "title",
        "for_person",
        "added_by",
        "gift_date",
        "price",
        "status",
        "created_at",
    )

    list_filter = (
        "status",
        "gift_date",
    )

    search_fields = (
        "title",
        "description",
        "for_person__username",
        "added_by__username",
    )

    ordering = (
        "-created_at",
    )