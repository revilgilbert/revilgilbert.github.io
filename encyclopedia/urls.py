from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("create", views.create, name="create"),
    path("save", views.save, name="save"),
    path("search", views.search, name="search"),
    path("edit/<str:title>", views.edit, name="edit"),
    path("wiki/<str:title>", views.entry, name="entry"),
    path("random", views.randomentry, name="random"),
]