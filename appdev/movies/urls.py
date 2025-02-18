from django.urls import path
from .views import MovieListView, MovieDetailView

urlpatterns = [
    path('', MovieListView.as_view(), name='movie-list'),  # Home page with movie list
    path('movie/<int:pk>/', MovieDetailView.as_view(), name='movie-detail'),  # Movie detail page
]

from django.urls import path
from .views import MovieListView, MovieDetailView, WatchlistView, AddToWatchlistView, RateMovieView

urlpatterns = [
    path('', MovieListView.as_view(), name='movie-list'),  # Home page with movie list
    path('movie/<int:pk>/', MovieDetailView.as_view(), name='movie-detail'),  # Movie detail page
    path('watchlist/', WatchlistView.as_view(), name='watchlist'),  # User's watchlist
    path('add-to-watchlist/<int:movie_id>/', AddToWatchlistView.as_view(), name='add-to-watchlist'),  # Add movie to watchlist
    path('rate-movie/<int:movie_id>/', RateMovieView.as_view(), name='rate-movie'),  # Rate a movie
]