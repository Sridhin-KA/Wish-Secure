from django.urls import path
from . import views

urlpatterns=[

    path(
        '',
        views.wish_list,
        name="wish_list"
    ),

    path(
        'add/',
        views.add_wish,
        name="add_wish"
    ),

    path(
        'view/<int:id>/',
        views.view_wish,
        name="view_wish"
    ),

    path(
        'edit/<int:id>/',
        views.edit_wish,
        name="edit_wish"
    ),

    path(
        'delete/<int:id>/',
        views.delete_wish,
        name="delete_wish"
    ),
    path(
    'comment/<int:id>/',
    views.add_comment,
    name='add_comment'
),

    path(
        'complete/<int:id>/',
        views.complete_wish,
        name='complete_wish'
    ),

]