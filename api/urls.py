from django.urls import path
from . import views


urlpatterns = [
    path("posts/", views.BlogPostListCreate.as_view(), name="posts-view-create"),
    path("posts/<int:id>/", views.BlogPostRetrieveUpdateDestroy.as_view(), name="posts-view-retrieve-update-destroy"),
    path("postsfilter/",views.BlogPostList.as_view(), name="posts-view-filter"),
]