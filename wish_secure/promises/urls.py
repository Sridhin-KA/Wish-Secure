from django.urls import path

from . import views


urlpatterns = [

    path(
        "",
        views.promise_list,
        name="promise_list"
    ),

    path(
        "add/",
        views.add_promise,
        name="add_promise"
    ),

    path(
        "view/<int:id>/",
        views.view_promise,
        name="view_promise"
    ),

    path(
        "edit/<int:id>/",
        views.edit_promise,
        name="edit_promise"
    ),

    path(
        "delete/<int:id>/",
        views.delete_promise,
        name="delete_promise"
    ),

    path(
        "keep/<int:id>/",
        views.keep_promise,
        name="keep_promise"
    ),

]