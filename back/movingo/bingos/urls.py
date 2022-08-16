from django.urls import path
from . import views
app_name="bingos"

urlpatterns = [
    path('current/', views.get_current_bingo)
]
