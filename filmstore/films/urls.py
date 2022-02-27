from django.urls import path, include
from rest_framework import routers

from films.views import film_index, users, index, director_create, director_detail, director_edit, get_all_directors, \
    genre_create, genre_detail, genre_edit, get_all_genres, movie_create, movie_detail, movie_edit, get_all_movies, \
    director_search, movie_search, genre_search
from films.views import GenreViewSet, MovieViewSet, DirectorViewSet

router = routers.DefaultRouter()
router.register(r'genres', GenreViewSet)
router.register(r'movies', MovieViewSet)
router.register(r'directors', DirectorViewSet)

urlpatterns = [
    path('', index, name='index'),

    path('director/new/', director_create, name='director_create'),
    path('director/all', get_all_directors, name='directors_list'),
    path('director/<int:pk>/', director_detail, name='director_detail'),
    path('director/<int:pk>/edit/', director_edit, name='director_edit'),
    path('director/search', director_search, name='director_search_list'),

    path('genre/new', genre_create, name='genre_create'),
    path('genre/all', get_all_genres, name='genre_list'),
    path('genre/<int:pk>/', genre_detail, name='genre_detail'),
    path('genre/<int:pk>/edit/', genre_edit, name='genre_edit'),
    path('genre/search', genre_search, name='genre_search_list'),

    path('movie/new', movie_create, name='movie_create'),
    path('movie/all', get_all_movies, name='movie_list'),
    path('movie/<int:pk>/', movie_detail, name='movie_detail'),
    path('movie/<int:pk>/edit/', movie_edit, name='movie_edit'),
    path('movie/search', movie_search, name="movie_search_list"),

    path('<int:film_id>', film_index),
    path('<int:user_id>; <str:user_name>', users),
    # path('social_auth/')

    path("api/", include(router.urls))
]
