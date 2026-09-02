from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.utils import timezone

from .models import Promise
from .forms import PromiseForm


# =========================
# PROMISE LIST
# =========================

@login_required
def promise_list(request):

    promises = Promise.objects.select_related(
        "made_by"
    ).order_by("-promise_date")

    return render(
        request,
        "promises/promise_list.html",
        {
            "promises": promises
        }
    )


# =========================
# ADD PROMISE
# =========================

@login_required
def add_promise(request):

    if request.method == "POST":

        form = PromiseForm(request.POST)

        if form.is_valid():

            promise = form.save(commit=False)

            promise.made_by = request.user

            promise.save()

            messages.success(
                request,
                "Your promise has been saved ❤️"
            )

            return redirect("promise_list")

    else:

        form = PromiseForm()

    return render(
        request,
        "promises/add_promise.html",
        {
            "form": form
        }
    )


# =========================
# VIEW PROMISE
# =========================

@login_required
def view_promise(request, id):

    promise = get_object_or_404(
        Promise,
        id=id
    )

    return render(
        request,
        "promises/view_promise.html",
        {
            "promise": promise
        }
    )


# =========================
# EDIT PROMISE
# =========================

@login_required
def edit_promise(request, id):

    promise = get_object_or_404(
        Promise,
        id=id
    )

    if promise.made_by != request.user:

        messages.error(
            request,
            "You can only edit your own promises."
        )

        return redirect(
            "promise_list"
        )

    if request.method == "POST":

        form = PromiseForm(
            request.POST,
            instance=promise
        )

        if form.is_valid():

            form.save()

            messages.success(
                request,
                "Promise updated successfully ❤️"
            )

            return redirect(
                "view_promise",
                id=promise.id
            )

    else:

        form = PromiseForm(
            instance=promise
        )

    return render(
        request,
        "promises/edit_promise.html",
        {
            "form": form,
            "promise": promise
        }
    )


# =========================
# DELETE PROMISE
# =========================

@login_required
def delete_promise(request, id):

    promise = get_object_or_404(
        Promise,
        id=id
    )

    if promise.made_by != request.user:

        messages.error(
            request,
            "You can only delete your own promises."
        )

        return redirect(
            "promise_list"
        )

    if request.method == "POST":

        promise.delete()

        messages.success(
            request,
            "Promise deleted."
        )

        return redirect(
            "promise_list"
        )

    return render(
        request,
        "promises/delete_promise.html",
        {
            "promise": promise
        }
    )


# =========================
# MARK AS KEPT
# =========================

@login_required
def keep_promise(request, id):

    promise = get_object_or_404(
        Promise,
        id=id
    )

    if promise.status == "Active":

        promise.status = "Kept"

        promise.kept_at = timezone.now()

        promise.save(
            update_fields=[
                "status",
                "kept_at",
                "updated_at",
            ]
        )

        messages.success(
            request,
            "Promise kept ❤️"
        )

    return redirect(
        "view_promise",
        id=promise.id
    )