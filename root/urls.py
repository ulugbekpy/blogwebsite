from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include
from users import views as user_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('app.urls')),

    path('register1/', user_views.registration1, name='register'),
    path('register2/', user_views.registration2, name='step2'),
    path('login/',
         auth_views.LoginView.as_view(template_name='users/login.html'),
         name='login'),
    path('logout/',
         auth_views.LogoutView.as_view(template_name='users/logout.html'),
         name='logout'),

    path('password-reset/',
         auth_views.PasswordResetView.as_view(
             template_name='users/password_reset.html'),
         name='password_reset'),

    path('password-reset/done/',
         auth_views.PasswordResetDoneView.as_view(
             template_name='users/password_reset_done.html'),
         name='password_reset_done'),

    path('password-reset-confirm/<uidb64>/<token>/',
         auth_views.PasswordResetConfirmView.as_view(
             template_name='users/password_reset_confirm.html'),
         name='password_reset_confirm'),

    path('password-reset-complete/',
         auth_views.PasswordResetCompleteView.as_view(
             template_name='users/password_reset_complete.html'),
         name='password_reset_complete'),

    path('me/', user_views.me, name='me'),

    path('users/profile/', user_views.profile, name='profile'),
    path('users/profiles/', user_views.UserListView.as_view(), name='profiles'),

    path('like/<int:id>/', user_views.like, name='like-one'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
