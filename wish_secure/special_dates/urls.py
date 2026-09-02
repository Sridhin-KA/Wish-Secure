from django.urls import path

from . import views


urlpatterns = [

    path(
        "",
        views.date_list,
        name="date_list"
    ),

    path(
        "add/",
        views.add_date,
        name="add_date"
    ),

    path(
        "view/<int:id>/",
        views.view_date,
        name="view_date"
    ),

    path(
        "edit/<int:id>/",
        views.edit_date,
        name="edit_date"
    ),

    path(
        "delete/<int:id>/",
        views.delete_date,
        name="delete_date"
    ),

]