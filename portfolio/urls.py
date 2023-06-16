from django.urls import path
from . import views

urlpatterns = [
    path("", views.index_view, name="index"),
    path("playground/", views.playground_view, name="playground"),
    path("blog/", views.blog_view, name="blog"),
    path("blog/<int:artigo_id>", views.article_view, name="article"),
    path("blog/like/<int:artigo_id>", views.like_view, name="like"),
    path("blog/comment/<int:artigo_id>", views.comment_view, name="comment"),
    path("blog/comment/<int:comentario_id>/like", views.comment_like_view, name="comment_like"),
    path("blog/delete/<int:artigo_id>", views.delete_article_view, name="delete"),
    path("admin/", views.admin_view, name="admin"),
    path("blog/new/", views.new_article_view, name="new"),
    path("blog/edit/<int:artigo_id>", views.edit_article_view, name="edit"),
    path("login/", views.login_view, name="login"),
    path("login/<str:url>", views.login_view, name="login_args")
]
