from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
from django.views.decorators.http import require_http_methods
from django.core.files.uploadhandler import TemporaryFileUploadHandler

from rest_framework.generics import get_object_or_404, RetrieveAPIView, RetrieveUpdateAPIView, ListCreateAPIView

from .models import Director, Movie, Genre
from .forms import DirectorForm, MovieForm, GenreForm
from .serializers import DirectorSerializer, GenreSerializer, MovieSerializer


class DirectorDetail(RetrieveUpdateAPIView):
    serializer_class = DirectorSerializer
    queryset = Director.objects.all()


class DirectorCreateUpdateList(ListCreateAPIView):
    serializer_class = DirectorSerializer
    queryset = Director.objects.all()

    def perform_create(self, serializer):
        serializer.save(creator=self.request.user)


class DirectorDetailAPIView(RetrieveAPIView):
    serializer_class = DirectorSerializer
    queryset = Director.objects.all()


class MovieDetail(RetrieveUpdateAPIView):
    serializer_class = MovieSerializer

    queryset = Movie.objects.all()


class MovieList(ListCreateAPIView):
    serializer_class = MovieSerializer
    queryset = Movie.objects.all()


class GenreDetail(RetrieveUpdateAPIView):
    serializer_class = GenreSerializer
    queryset = Genre.objects.all()


class GenreList(ListCreateAPIView):
    serializer_class = GenreSerializer
    queryset = Genre.objects.all()


@require_http_methods(["GET", "POST"])
def index(request):
    return render(request, "base.html")


@require_http_methods(["POST", "GET"])
def director_create(request):
    if request.method == "POST":
        form = DirectorForm(request.POST)
        if form.is_valid():
            director = form.save(commit=False)
            director.full_name = request.POST.get('full_name')
            director.birth_date = request.POST.get('birth_date')
            director.age = request.POST.get('age')
            director.death_date = request.POST.get('death_date')
            director.save()
            return redirect('director_detail', pk=director.pk)
    else:
        form = DirectorForm()
    return render(request, 'director_edit.html', {'form': form})


@require_http_methods(["POST", "GET"])
def director_edit(request, pk):
    director = get_object_or_404(Director, pk=pk)
    if request.method == "POST":
        form = DirectorForm(request.POST, instance=director)
        if form.is_valid():
            director = form.save(commit=False)
            director.full_name = request.POST.get('full_name')
            director.birth_date = request.POST.get('birth_date')
            director.age = request.POST.get('age')
            director.death_date = request.POST.get('death_date')
            request.upload_handlers = [TemporaryFileUploadHandler(request=request)]
            director.cover = request.POST.get('cover')
            director.save()
            return redirect('director_detail', pk=director.pk)
    else:
        form = DirectorForm(instance=director)
    return render(request, 'director_edit.html', {'form': form})


@require_http_methods(["GET", "POST"])
def director_detail(request, pk):
    director = get_object_or_404(Director, pk=pk)
    if request.method == "GET":
        return render(request, 'director_detail.html', {'director': director})
    elif request.method == "POST":
        director.delete()
        return redirect('index')


@require_http_methods(["GET"])
def get_all_directors(request):
    return render(request, 'directors.html', {'directors': Director.objects.all()})


@require_http_methods(["POST", "GET"])
def genre_create(request):
    if request.method == "POST":
        form = GenreForm(request.POST)
        if form.is_valid():
            genre = form.save(commit=False)
            genre.name = request.POST.get('name')
            genre.save()
            return redirect('genre_detail', pk=genre.pk)
    else:
        form = GenreForm()
    return render(request, 'genre_edit.html', {'form': form})


@require_http_methods(["POST", "GET"])
def genre_edit(request, pk):
    genre = get_object_or_404(Genre, pk=pk)
    if request.method == "POST":
        form = GenreForm(request.POST, instance=genre)
        if form.is_valid():
            genre = form.save(commit=False)
            genre.name = request.POST.get('name')
            genre.save()
            return redirect('genre_detail', pk=genre.pk)
    else:
        form = GenreForm(instance=genre)
    return render(request, 'genre_edit.html', {'form': form})


@require_http_methods(["GET", "POST"])
def genre_detail(request, pk):
    genre = get_object_or_404(Genre, pk=pk)
    if request.method == "GET":
        return render(request, 'genre_detail.html', {'genre': genre})
    elif request.method == "POST":
        genre.delete()
        return redirect('index')


@require_http_methods(["GET"])
def get_all_genres(request):
    return render(request, 'genres.html', {'genres': Genre.objects.all()})
    # return JsonResponse(list(Genre.objects.all()))


@require_http_methods(["POST", "GET"])
def movie_create(request):
    if request.method == "POST":
        form = MovieForm(request.POST)
        if form.is_valid():
            movie = form.save(commit=False)
            movie.save()
            form.save_m2m()
            return redirect('movie_detail', pk=movie.pk)
    else:
        form = MovieForm()
    return render(request, 'movie_edit.html', {'form': form})


@require_http_methods(["POST", "GET"])
def movie_edit(request, pk):
    movie = get_object_or_404(Movie, pk=pk)
    if request.method == "POST":
        form = MovieForm(request.POST, instance=movie)
        if form.is_valid():
            movie = form.save(commit=False)
            movie.title = request.POST.get('title')
            movie.release_year = request.POST.get('release_year')
            movie.price = request.POST.get('price')
            movie.directors.set(request.POST.get('directors'))
            movie.genres.set(request.POST.get('genres'))
            movie.save()
            return redirect('movie_detail', pk=movie.pk)
    else:
        form = MovieForm(instance=movie)
    return render(request, 'movie_edit.html', {'form': form})


@require_http_methods(["GET", "POST"])
def movie_detail(request, pk):
    movie = get_object_or_404(Movie, pk=pk)
    if request.method == "GET":
        return render(request, 'movie_detail.html', {'movie': movie})
    elif request.method == "POST":
        movie.delete()
        return redirect('index')


@require_http_methods(["GET"])
def get_all_movies(request):
    return render(request, 'movies.html', {'movies': Movie.objects.all()})


@require_http_methods(["GET"])
def director_search(request):

    return render(request, 'director_search.html')


@require_http_methods(["GET", "POST"])
def movie_search(request):
    if request.method == "POST":
        searched = request.POST.get('searched')
        movies = Movie.objects.filter(title__icontains=searched)
        return render(request, 'movie_search.html', {'searched': searched, 'movies': movies})
    else:
        return render(request, 'movie_search.html', {})


@require_http_methods(["GET"])
def genre_search(request):
    return render(request, 'genre_search.html')


def film_index(request, film_id):
    print(f"film_id={film_id}")
    return HttpResponse(f"<html><head/><body><h1>Film #{film_id}</h1></body></html>")


def users(request, id, name):
    output = "<h2>Пользователь</h2><h3>id: {0}" \
             "Имя:{1}</h3>".format(id, name)
    return HttpResponse(output)







#
# @require_http_methods(["POST"])
# def create_movie(request):
#     form = MovieForm(request.POST)
#     if form.is_valid():
#         movie = form.save()
#         return JsonResponse({
#             'msg': 'Фильм сохранён'
#         })
#     return JsonResponse({'errors': form.errors}, status=400)


# @require_http_methods(["POST", "GET"])
# def create_director(request):
#     print(request.method)
#     if request.method == "POST":
#         form = DirectorForm(request.POST)
#         if form.is_valid():
#             movie = form.save()
#             return JsonResponse({
#                 'msg': 'Режиссёр сохранён',
#                 'id': movie.id,
#             })
#     else:
#         form = DirectorForm()
#     return render(request, 'director_edit.html', {'form': form})


# @require_http_methods(["POST"])
# def create_genre(request):
#     form = GenreForm(request.POST)
#     if form.is_valid():
#         movie = form.save()
#         return JsonResponse({
#             'msg': 'Жанр сохранён'
#         })
#     return JsonResponse({'errors': form.errors}, status=400)

# @require_http_methods(["POST"])
# def update_user_data(request):
#     try:
#         user_id = request.GET.get('id')
#         user_to_be_updated = User.objects.get(id=user_id)
#     except User.DoesNotExist:
#         raise Http404
#     return JsonResponse(list(user_to_be_updated), safe=True)





