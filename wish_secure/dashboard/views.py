from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.contrib.auth.decorators import login_required

from wishes.models import Wish, WishComment,Activity, Category
from special_dates.models import SpecialDate


@login_required
def dashboard(request):

    # =========================
    # WISH STATISTICS
    # =========================

    total = Wish.objects.count()

    completed = Wish.objects.filter(
        status="Completed"
    ).count()

    pending = Wish.objects.exclude(
        status="Completed"
    ).count()

    comments = WishComment.objects.count()


    # =========================
    # LATEST WISHES
    # =========================

    my_latest = Wish.objects.filter(
        created_by=request.user
    ).order_by("-created_at").first()

    partner_latest = Wish.objects.exclude(
        created_by=request.user
    ).order_by("-created_at").first()


    # =========================
    # ACTIVITY
    # =========================

    activities = Activity.objects.select_related(
        "user",
        "wish"
    ).order_by("-created_at")[:10]

    unread_notifications = Activity.objects.filter(
        is_read=False
    ).exclude(
        user=request.user
    ).count()


    # =========================
    # SPECIAL DATES
    # =========================

    special_dates = SpecialDate.objects.all()

    next_special_date = None

    for special_date in special_dates:

        special_date.next_date = special_date.next_occurrence()
        special_date.remaining_days = special_date.days_until()

        if next_special_date is None:
            next_special_date = special_date

        elif special_date.next_date < next_special_date.next_date:
            next_special_date = special_date


    # =========================
    # CONTEXT
    # =========================

    context = {

        "total": total,

        "completed": completed,

        "pending": pending,

        "comments": comments,

        "my_latest": my_latest,

        "partner_latest": partner_latest,

        "activities": activities,

        "unread_notifications": unread_notifications,

        "next_special_date": next_special_date,

    }

    return render(
        request,
        "dashboard/dashboard.html",
        context
    )