from django.contrib import admin
from django.conf.urls import url
from django.urls import path, include
from . import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf.urls.static import static
from django.conf import settings
from django.contrib.auth import views as auth_views
from django.urls import reverse_lazy
urlpatterns = [
    path('admin/', admin.site.urls),
    path('events/', include('events.urls')),
    path('accounts/', include('accounts.urls')),
    path('calendar/', include('cals.urls')),
    path('posts/', include('posts.urls')),
    path('', views.home, name="home_page"),
    path('team', views.teams, name="team"),
    path('register', views.reg_form, name="reg_form"),
    path('rewards', views.rewards_1_view, name="rewards"),

    # for resetting password functionality
    path('reset_password/',
         auth_views.PasswordResetView.as_view(
             template_name="password_reset.html"),
         name="reset_password"),

    path('reset_password_sent/',
         auth_views.PasswordResetDoneView.as_view(
             template_name="password_reset_sent.html"),
         name="password_reset_done"),

    path('reset/<uidb64>/<token>/',
         auth_views.PasswordResetConfirmView.as_view(
             template_name="password_reset_form.html"),
         name="password_reset_confirm"),

    path('reset_password_complete/',
         auth_views.PasswordResetCompleteView.as_view(
             template_name="password_reset_done.html"),
         name="password_reset_complete"),
]
urlpatterns += staticfiles_urlpatterns()
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
