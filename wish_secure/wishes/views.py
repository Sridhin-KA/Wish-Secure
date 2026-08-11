from django.shortcuts import render,redirect,get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.utils import timezone
from .models import *
from .forms import *
from django.db.models import Count


@login_required
def wish_list(request):

    wishes = Wish.objects.all()

    search = request.GET.get("search")
    priority = request.GET.get("priority")
    category = request.GET.get("category")
    status = request.GET.get("status")
    sort = request.GET.get("sort")

    if search:
        wishes = wishes.filter(title__icontains=search)

    if priority:
        wishes = wishes.filter(priority=priority)

    if category:
        wishes = wishes.filter(category_id=category)

    if status:
        wishes = wishes.filter(status=status)

    if sort == "old":

        wishes = wishes.order_by("created_at")

    else:

        wishes = wishes.order_by("-created_at")

    context = {

        "wishes": wishes,
        "categories": Category.objects.all(),

        "search": search,
        "priority": priority,
        "status": status,
        "category": category,
        "sort": sort

    }

    return render(
        request,
        "wishes/wish_list.html",
        context
    )

@login_required
def add_wish(request):

    categories = Category.objects.all()

    if request.method == "POST":

        title = request.POST.get("title")
        description = request.POST.get("description")
        category = request.POST.get("category")
        priority = request.POST.get("priority")
        visibility = request.POST.get("visibility")

        image = request.FILES.get("image")

        wish = Wish.objects.create(

            title=title,

            description=description,

            category=Category.objects.get(id=category),

            priority=priority,

            visibility=visibility,

            image=image,

            created_by=request.user

        )
        wish.save
        Activity.objects.create(
        user=request.user,
        wish=wish,
        action='added',
        message=f'{request.user.first_name} added a new wish'
)
        messages.success(request,"Wish Added ❤️")

        return redirect("wish_list")

    context = {

        "categories":categories

    }

    return render(
        request,
        "wishes/add_wish.html",
        context
    )
@login_required
def view_wish(request,id):

    wish=get_object_or_404(
        Wish,
        id=id
    )

    if wish.visibility=="Private" and wish.created_by!=request.user:

        messages.error(
            request,
            "This wish is private."
        )

        return redirect("wish_list")

    return render(
        request,
        "wishes/view_wish.html",
        {
            "wish":wish
        }
    )
    
@login_required
def edit_wish(request,id):

    wish=get_object_or_404(
        Wish,
        id=id
    )

    if request.user!=wish.created_by:

        messages.error(
            request,
            "Only creator can edit."
        )

        return redirect("wish_list")

    form=WishForm(instance=wish)

    if request.method=="POST":

        form=WishForm(
            request.POST,
            request.FILES,
            instance=wish
        )

        if form.is_valid():

            form.save()

            messages.success(
                request,
                "Wish Updated ❤️"
            )

            return redirect("wish_list")

    context={

        "form":form

    }

    return render(
        request,
        "wishes/edit_wish.html",
        context
    )


@login_required
def delete_wish(request,id):

    wish=get_object_or_404(
        Wish,
        id=id
    )

    if request.user==wish.created_by:

        wish.delete()

        messages.success(
            request,
            "Wish Deleted"
        )

    return redirect("wish_list")

@login_required
def add_comment(request, id):

    wish = get_object_or_404(
        Wish,
        id=id
    )

    if wish.visibility == "Private" and wish.created_by != request.user:

        messages.error(
            request,
            "This wish is private."
        )

        return redirect(
            "wish_list"
        )

    if request.method == "POST":

        comment = request.POST.get("comment")

        if comment:

            WishComment.objects.create(

                wish=wish,

                user=request.user,

                comment=comment

            )

            Activity.objects.create(

                user=request.user,

                wish=wish,

                action="commented",

                message=f'{request.user.first_name} commented on {wish.title}'

            )

    return redirect(
        "view_wish",
        id=id
    )
    
@login_required
def complete_wish(request, id):

    wish = get_object_or_404(
        Wish,
        id=id
    )

    if wish.status != "Completed":

        wish.status = "Completed"

        wish.completed_by = request.user

        wish.completed_at = timezone.now()

        wish.save()

        Activity.objects.create(

            user=request.user,

            wish=wish,

            action="completed",

            message=f'{request.user.first_name} completed {wish.title}'

        )

        messages.success(
            request,
            "Wish completed ❤️"
        )

    return redirect(
        "view_wish",
        id=id
    )