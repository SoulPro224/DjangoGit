from django.urls import path
from .views import PostListView, PostDetailView, PostCreateView, PostUpdateView, PostDeleteView, TagPostListView, CategoryPostListView

app_name = 'blog'
urlpatterns = [
    path('', PostListView.as_view(), name='home'),
    path('post/<int:pk>/', PostDetailView.as_view(), name='post_detail'),
    path('post_form/', PostCreateView.as_view(), name='post_create'),
    path('post/<int:pk>/edit/', PostUpdateView.as_view(), name='post_edit'),
    path('post/<int:pk>/delete/', PostDeleteView.as_view(), name='post_delete'),
    path('category/<str:category_name>/', CategoryPostListView.as_view(), name='category_post_list'),
    path('tags/<str:tag_name>/', TagPostListView.as_view(), name='tag_list'),
]
