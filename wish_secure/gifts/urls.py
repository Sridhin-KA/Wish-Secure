from django.urls import path

from . import views


urlpatterns = [

    path(
        "",
        views.gift_list,
        name="gift_list"
    ),

    path(
        "add/",
        views.add_gift,
        name="add_gift"
    ),

    path(
        "view/<int:id>/",
        views.view_gift,
        name="view_gift"
    ),

    path(
        "edit/<int:id>/",
        views.edit_gift,
        name="edit_gift"
    ),

    path(
        "delete/<int:id>/",
        views.delete_gift,
        name="delete_gift"
    ),

]