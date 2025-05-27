from django.urls import path
from .views import PostListCreateAPIView, PostRetrieveAPIView

urlpatterns = [
    # 記事取得のためのURL
    path('posts/', PostListCreateAPIView.as_view(), name='post-list-create'),
    # CRUD処理のためのURL
    path('posts/<int:pk>/', PostRetrieveAPIView.as_view(), name='post-detail'),
]