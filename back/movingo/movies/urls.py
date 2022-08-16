from django.urls import path
from . import views

app_name="movies"

urlpatterns = [
    path('', views.movie_list),
    path('<int:movie_pk>', views.movie_detail),
    path('<int:movie_pk>/review/', views.create_review),
    path('<int:movie_pk>/reviews/', views.movie_review_list),
    path('<int:movie_pk>/reviews/<int:review_pk>', views.like_update_delete_review),
    path('<int:movie_pk>/wish/', views.wish_movie),
    path('<int:movie_pk>/collections/', views.movie_collections),
    path('search/<keyword>/', views.auto_complete),
]
