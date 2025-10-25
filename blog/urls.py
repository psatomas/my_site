from django.urls import path

from . import views

urlpatterns = [
    path("", views.starting_page, name="starting-page"),
    path("posts", views.posts, name="post-page"),
    path("post/<slug:slug>", views.post_detail, name="post_detail_page")
]