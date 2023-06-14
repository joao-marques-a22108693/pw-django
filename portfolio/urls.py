from django.urls import path
from . import views

urlpatterns = [
    path("", views.index_view, name="index"),
    path("playground/", views.playground_view, name="playground"),
    path("blog/", views.blog_view, name="blog"),
    path("blog/<int:id>", views.article_view, name="article"),
    path("admin/", views.admin_view, name="admin"),
    path("new/", views.new_article_view, name="new")
]
