from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages

from .models import Gift
from .forms import GiftForm


# =========================
# GIFT LIST
# =========================

@login_required
def gift_list(request):

    gifts = Gift.objects.select_related(
        "for_person",
        "added_by"
    ).order_by("-created_at")

    return render(
        request,
        "gifts/gift_list.html",
        {
            "gifts": gifts
        }
    )


# =========================
# ADD GIFT
# =========================

@login_required
def add_gift(request):

    if request.method == "POST":

        form = GiftForm(
            request.POST,
            request.FILES
        )

        if form.is_valid():

            gift = form.save(
                commit=False
            )

            gift.added_by = request.user

            gift.save()

            messages.success(
                request,
                "Gift saved successfully 🎁❤️"
            )

            return redirect(
                "gift_list"
            )

    else:

        form = GiftForm()

    return render(
        request,
        "gifts/add_gift.html",
        {
            "form": form
        }
    )


# =========================
# VIEW GIFT
# =========================

@login_required
def view_gift(request, id):

    gift = get_object_or_404(
        Gift,
        id=id
    )

    return render(
        request,
        "gifts/view_gift.html",
        {
            "gift": gift
        }
    )


# =========================
# EDIT GIFT
# =========================

@login_required
def edit_gift(request, id):

    gift = get_object_or_404(
        Gift,
        id=id
    )

    if gift.added_by != request.user:

        messages.error(
            request,
            "You can only edit gifts you added."
        )

        return redirect(
            "gift_list"
        )

    if request.method == "POST":

        form = GiftForm(
            request.POST,
            request.FILES,
            instance=gift
        )

        if form.is_valid():

            form.save()

            messages.success(
                request,
                "Gift updated successfully ❤️"
            )

            return redirect(
                "view_gift",
                id=gift.id
            )

    else:

        form = GiftForm(
            instance=gift
        )

    return render(
        request,
        "gifts/edit_gift.html",
        {
            "form": form,
            "gift": gift
        }
    )


# =========================
# DELETE GIFT
# =========================

@login_required
def delete_gift(request, id):

    gift = get_object_or_404(
        Gift,
        id=id
    )

    if gift.added_by != request.user:

        messages.error(
            request,
            "You can only delete gifts you added."
        )

        return redirect(
            "gift_list"
        )

    if request.method == "POST":

        gift.delete()

        messages.success(
            request,
            "Gift removed."
        )

        return redirect(
            "gift_list"
        )

    return render(
        request,
        "gifts/delete_gift.html",
        {
            "gift": gift
        }
    )