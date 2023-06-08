from django.urls import path
from . import views

urlpatterns = [
    path("", views.index_view, name="index"),
    path("blog/", views.blog_view, name="blog"),
    path("admin/", views.admin_view, name="admin"),
    path("new/", views.new_article_view, name="new")
]
