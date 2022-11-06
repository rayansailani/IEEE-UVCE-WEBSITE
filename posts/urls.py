from django.urls import path
from django.conf.urls import url
from . import views


urlpatterns = [
    path('', views.post_view, name='post'),
    path('create', views.create_post_view, name="createPost"),
    path('<int:id>', views.detail_view, name='detail'),
]
