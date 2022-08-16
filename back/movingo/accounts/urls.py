from . import views
from django.urls import path

app_name="accounts"

urlpatterns = [
    path('currentuser/', views.current_user), 
    path('profile/<int:user_pk>/follow/', views.follow),
    path('profile/reviews/<int:review_pk>/', views.user_review),
    path('profile/<username>/', views.profile),
    path('profile/<username>/update/,', views.profile),
]