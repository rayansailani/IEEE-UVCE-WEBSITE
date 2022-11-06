from django.urls import path
from django.conf.urls import url
from . import views

app_name = 'articles'

urlpatterns = [
    path('', views.events_list, name='list'),
    path('create', views.event_create, name='create'),
    path('update/', views.create_update, name="update"),
    path('db', views.student_view, name="s_dashboard"),
    path('db_ev', views.sig_view, name="dashboard"),
    url(r'^(?P<slug>[\w-]+)/$', views.event_detail, name='detail'),
    path('<slug>/edit', views.edit_view, name='edit'),
    path('<slug>/delete', views.delete_view, name="delete"),
    path('<slug>/approve', views.approve_view, name="approve"),
    path('evold', views.old_events_view, name='old_events'),

]
