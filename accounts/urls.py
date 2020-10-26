from django.urls import path
from . import views

from django.urls import reverse_lazy
app_name = 'accounts'

urlpatterns = [
    path('login/', views.login_view, name='login'),
    path('logout', views.logout_view, name='logout'),
    path('register', views.register_view, name='register'),
]
