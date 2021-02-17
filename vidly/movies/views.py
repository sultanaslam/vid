from django.shortcuts import get_object_or_404,render
from .models import Movie
# Create your views here.
def index(request):
    movies = Movie.objects.all()
    # output = ', '.join([m.title for m in movies])
    # return HttpResponse('HELLO')
    return render(request, 'index.html', {'movies': movies})

def details(request, movie_id):
    movie = get_object_or_404(Movie, pk=movie_id)
    return render(request, 'movie.html', {'movie':movie})
