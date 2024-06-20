from django.urls import path
from . import views

app_name = "core"
urlpatterns = [
    path("", views.index, name="home"),
    path("movies/<tmdb_id>", views.movie_detail_view, name="movie_detail"), 
]