from django.urls import path
from community import views

app_name="community"

urlpatterns = [
    path('', views.threads_or_create),
    path('create/<int:movie_pk>/', views.create_thread),
    path('<int:thread_pk>/', views.thread_read_delete),
    path('moviethread/<int:movie_pk>/', views.thread_exists),
    path('<int:thread_pk>/comment/', views.create_comment),
    path('<int:thread_pk>/comment/<int:comment_pk>/', views.comment_ud)
]