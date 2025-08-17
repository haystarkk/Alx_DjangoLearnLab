from django.urls import path
from .views import (
    PostListView, PostDetailView,
    PostCreateView, PostUpdateView, PostDeleteView,
    CommentCreateView, CommentUpdateView, CommentDeleteView,
    UserPostListView, register, user_login, user_logout, profile
)
from .views import TaggedPostListView, SearchResultsView

urlpatterns = [
    # Post URLs
    path('', PostListView.as_view(), name='blog-home'),
    path('post/<int:pk>/', PostDetailView.as_view(), name='post-detail'),
    path('post/new/', PostCreateView.as_view(), name='post-create'),
    path('post/<int:pk>/update/', PostUpdateView.as_view(), name='post-update'),
    path('post/<int:pk>/delete/', PostDeleteView.as_view(), name='post-delete'),
    
    # Comment URLs with requested pattern
    path('post/<int:pk>/comments/new/', CommentCreateView.as_view(), name='comment-create'),
    path('comment/<int:pk>/update/', CommentUpdateView.as_view(), name='comment-update'),
    path('comment/<int:pk>/delete/', CommentDeleteView.as_view(), name='comment-delete'),
    
    # User URLs
    path('user/<str:username>/', UserPostListView.as_view(), name='user-posts'),
    
    # Auth URLs
    path('register/', register, name='register'),
    path('login/', user_login, name='login'),
    path('logout/', user_logout, name='logout'),
    path('profile/', profile, name='profile'),
]
urlpatterns = [
    ...
    path('tags/<slug:tag>/', TaggedPostListView.as_view(), name='tagged-posts'),
    path('search/', SearchResultsView.as_view(), name='search-results'),
    ...
]
