from django.shortcuts import render, get_object_or_404
from .models import Movie


def movie_list(request):
    sort = request.GET.get("sort", "title")
    direction = request.GET.get("dir", "asc")  # asc or desc

    ordering_map = {
        "title": "title",
        "genre": "genre__name",
        "price": "daily_rental_rate",
    }

    order_by = ordering_map.get(sort, "title")
    if direction == "desc":
        order_by = f"-{order_by}"

    movies = Movie.objects.select_related("genre").order_by(order_by)

    return render(
        request,
        "movies/movie_list.html",
        {
            "movies": movies,
            "sort": sort,
            "direction": direction,
        },
    )


def movie_detail(request, pk):
    movie = get_object_or_404(Movie.objects.select_related("genre"), pk=pk)
    return render(request, "movies/movie_detail.html", {"movie": movie})
