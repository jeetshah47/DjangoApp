from django.shortcuts import render,get_object_or_404
from django.http import HttpResponse,Http404

# Create your views here.
from .models import Movie


def index(request):
    movies = Movie.objects.all()
    return render(request, 'movies/index.html', {'movies': movies})


def detail(request, movie_id):
    movie = get_object_or_404(Movie, pk=movie_id)
    return render(request, 'movies/detail.html', {'movie': movie})


def secrets(request):
    return HttpResponse("Keep it under the wraps")
