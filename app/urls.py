from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from .views import (mainpage,
                    PostListView, PostDetailView,
                    PostUpdateView, PostCreateView,
                    PostDeleteView, UserPostListView,
                    CommentListView)

urlpatterns = [
    path('', mainpage, name='main-page'),
    path('post/new/', PostCreateView.as_view(template_name="app/post_create.html"),
         name='post-create'),
    path('posts/', PostListView.as_view(), name='posts'),
    path('user-posts/<str:username>/',
         UserPostListView.as_view(), name='user-posts'),
    path('post/<int:pk>/update/',
         PostUpdateView.as_view(template_name="app/post_update.html"), name='post-update'),
    path('post/<int:pk>/', PostDetailView.as_view(), name='post-detail'),
    path('post/<int:pk>/delete/', PostDeleteView.as_view(), name='post-delete'),
    path('post/<int:pk>/comments', CommentListView.as_view(), name='comments'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
