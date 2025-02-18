from django.shortcuts import render

from django.views.generic import ListView, DetailView
from django.shortcuts import redirect, get_object_or_404
from .models import Movie, Watchlist, Rating
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator

class MovieListView(ListView):
    model = Movie
    template_name = 'movies/movie_list.html'

class MovieDetailView(DetailView):
    model = Movie
    template_name = 'movies/movie_detail.html'

@method_decorator(login_required, name='dispatch')
class WatchlistView(ListView):
    model = Watchlist
    template_name = 'movies/watchlist.html'

    def get_queryset(self):
        return Watchlist.objects.filter(user=self.request.user)

@method_decorator(login_required, name='dispatch')
class AddToWatchlistView(LoginRequiredMixin, DetailView):
    model = Movie

    def post(self, request, *args, **kwargs):
        movie = self.get_object()
        Watchlist.objects.get_or_create(user=request.user, movie=movie)
        return redirect('watchlist')

@method_decorator(login_required, name='dispatch')
class RateMovieView(LoginRequiredMixin, DetailView):
    model = Movie

    def post(self, request, *args, **kwargs):
        movie = self.get_object()
        score = request.POST.get('score')
        Rating.objects.update_or_create(user=request.user, movie=movie, defaults={'score': score})
        return redirect('movie-detail', pk=movie.pk)