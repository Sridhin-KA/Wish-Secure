from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.contrib.auth.decorators import login_required

from wishes.models import Wish, WishComment,Activity, Category

@login_required
def dashboard(request):

    total = Wish.objects.count()

    completed = Wish.objects.filter(
        status="Completed"
    ).count()

    pending = Wish.objects.exclude(
        status="Completed"
    ).count()

    comments = WishComment.objects.count()

    my_latest = Wish.objects.filter(
        created_by=request.user
    ).order_by("-created_at").first()

    partner_latest = Wish.objects.exclude(
        created_by=request.user
    ).order_by("-created_at").first()

    activities = Activity.objects.select_related(
        "user",
        "wish"
    ).order_by(
        "-created_at"
    )[:10]

    unread_notifications = Activity.objects.filter(
        is_read=False
    ).exclude(
        user=request.user
    ).count()

    context = {

        "total": total,

        "completed": completed,

        "pending": pending,

        "comments": comments,

        "my_latest": my_latest,

        "partner_latest": partner_latest,

        "activities": activities,

        "unread_notifications": unread_notifications,

    }

    return render(
        request,
        "dashboard/dashboard.html",
        context
    )