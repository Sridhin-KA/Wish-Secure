from django.contrib import admin
from .models import Promise


@admin.register(Promise)
class PromiseAdmin(admin.ModelAdmin):

    list_display = (
        "title",
        "made_by",
        "promise_date",
        "status",
        "created_at",
    )

    list_filter = (
        "status",
        "promise_date",
    )

    search_fields = (
        "title",
        "description",
        "made_by__username",
    )

    ordering = (
        "-promise_date",
    )