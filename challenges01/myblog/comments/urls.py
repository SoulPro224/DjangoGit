from django.urls import path
from .views import AddCommentView, CommentUpdateView, CommentDeleteView

app_name = 'comment'

urlpatterns = [
    path('add/<int:pk>/', AddCommentView.as_view(), name='add_comment'),
    path('update/<int:pk>/', CommentUpdateView.as_view(), name='comment_update'),
    path('delete/<int:pk>/', CommentDeleteView.as_view(), name='comment_delete'),
]
# path('post/<int:pk>/comment/', AddCommentView.as_view(), name='add_comment'),