from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from .views import mainpage,PostListView,PostDetailView,PostUpdateView,PostCreateView

urlpatterns = [
    path('',mainpage,name='main-page'),
    path('posts/',PostListView.as_view(),name='posts'),
    path('post/<int:pk>/',PostDetailView.as_view(),name='post-detail'),
    path('post/new/',PostCreateView.as_view(),name='post-create'),
    path('post/<int:pk>/',PostUpdateView.as_view(),name='post-update'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)