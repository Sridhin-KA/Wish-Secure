from django.contrib import admin

from .models import SpecialDate


@admin.register(SpecialDate)
class SpecialDateAdmin(admin.ModelAdmin):

    list_display = (
        "title",
        "date",
        "date_type",
        "repeat_yearly",
        "created_by",
    )

    list_filter = (
        "date_type",
        "repeat_yearly",
    )

    search_fields = (
        "title",
        "description",
    )