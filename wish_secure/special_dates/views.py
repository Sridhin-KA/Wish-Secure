from django.shortcuts import (
    render,
    redirect,
    get_object_or_404
)

from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.utils import timezone
from datetime import date
from .models import SpecialDate
from .forms import SpecialDateForm


@login_required
def date_list(request):

    dates = SpecialDate.objects.all()

    today = date.today()

    upcoming_dates = []
    past_dates = []

    for special_date in dates:

        special_date.next_date = (
            special_date.next_occurrence()
        )

        special_date.remaining_days = (
            special_date.days_until()
        )

        special_date.today = (
            special_date.is_today()
        )

        if special_date.repeat_yearly:

            upcoming_dates.append(special_date)

        elif special_date.date >= today:

            upcoming_dates.append(special_date)

        else:

            past_dates.append(special_date)

    upcoming_dates.sort(
    key=lambda x: x.next_date
)

    past_dates.sort(
        key=lambda x: x.date,
        reverse=True
    )

    return render(
        request,
        "special_dates/date_list.html",
        {
            "dates": upcoming_dates,
            "past_dates": past_dates
        }
    )

@login_required
def add_date(request):

    if request.method == "POST":

        form = SpecialDateForm(
            request.POST
        )

        if form.is_valid():

            special_date = form.save(
                commit=False
            )

            special_date.created_by = request.user

            special_date.save()

            messages.success(
                request,
                "Special date added ❤️"
            )

            return redirect(
                "date_list"
            )

    else:

        form = SpecialDateForm()

    return render(
        request,
        "special_dates/add_date.html",
        {
            "form": form
        }
    )


@login_required
def view_date(request, id):

    special_date = get_object_or_404(
        SpecialDate,
        id=id
    )

    return render(
        request,
        "special_dates/view_date.html",
        {
            "special_date": special_date
        }
    )


@login_required
def edit_date(request, id):

    special_date = get_object_or_404(
        SpecialDate,
        id=id
    )

    if special_date.created_by != request.user:

        messages.error(
            request,
            "You cannot edit this date."
        )

        return redirect(
            "date_list"
        )

    if request.method == "POST":

        form = SpecialDateForm(
            request.POST,
            instance=special_date
        )

        if form.is_valid():

            form.save()

            messages.success(
                request,
                "Special date updated ❤️"
            )

            return redirect(
                "date_list"
            )

    else:

        form = SpecialDateForm(
            instance=special_date
        )

    return render(
        request,
        "special_dates/edit_date.html",
        {
            "form": form,
            "special_date": special_date
        }
    )


@login_required
def delete_date(request, id):

    special_date = get_object_or_404(
        SpecialDate,
        id=id
    )

    if special_date.created_by == request.user:

        special_date.delete()

        messages.success(
            request,
            "Special date deleted."
        )

    else:

        messages.error(
            request,
            "You cannot delete this date."
        )

    return redirect(
        "date_list"
    )