from django.shortcuts import render
# from .fetch import get_popular_movies, get_movie_details, extract_movie_info, get_top_grossing_movies, API_KEY
from .utils import generate_star_html
from .models import Movie, GrossingMovie
# import requests
# Create your views here.

# def update_movie_videos():
#     movies = Movie.objects.all()

#     for movie in movies:
#         # Fetch videos for the movie using TMDB API
#         videos_url = f'https://api.themoviedb.org/3/movie/{movie.tmdb_id}/videos?api_key={API_KEY}'
#         response = requests.get(videos_url)
#         videos_data = response.json()

#         # Find a YouTube video URL
#         video_url = None
#         for video in videos_data['results']:
#             if video['site'] == 'YouTube':
#                 video_url = f"https://www.youtube.com/watch?v={video['key']}"
#                 break

#         # Update the movie with the video URL
#         if video_url:
#             movie.video_url = video_url
#             movie.save()

# def populate_movies():
#     popular_movies = get_popular_movies()
#     for movie in popular_movies:
#         movie_details = get_movie_details(movie['id'])
#         if movie_details:
#             movie_info = extract_movie_info(movie_details)
#             Movie.objects.update_or_create(
#                 tmdb_id=movie['id'],
#                 defaults={
#                     'title': movie['title'],
#                     'overview': movie['overview'],
#                     'popularity': movie['popularity'],
#                     'poster_path': movie['poster_path'],
#                     'backdrop_path': movie['backdrop_path'],
#                     'release_date': movie['release_date'],
#                     'genres': movie_info['genres'],
#                     'content_rating': movie_info['content_rating'],
#                     'release_date': movie['release_date'],
#                     'rating': movie['vote_average'],
#                 }
#             )

# def populate_grossing_movies():
#     top_grossing_movies = get_top_grossing_movies()
#     for movie in top_grossing_movies:
#         movie_details = get_movie_details(movie['id'])
#         if movie_details:
#             movie_info = extract_movie_info(movie_details)
#             GrossingMovie.objects.update_or_create(
#                 tmdb_id=movie['id'],
#                 defaults={
#                     'title': movie['title'],
#                     'overview': movie['overview'],
#                     'popularity': movie['popularity'],
#                     'poster_path': movie['poster_path'],
#                     'backdrop_path': movie['backdrop_path'],
#                     'release_date': movie['release_date'],
#                     'genres': movie_info['genres'],
#                     'content_rating': movie_info['content_rating'],
#                     'release_date': movie['release_date'],
#                     'rating': movie['vote_average'],
                
#                 }
#             )


# # # # # # # # # # #
#                   #
#      Views        #
#                   #
# # # # # # # # # # #

def index(request):
    # populate_movies()
    # populate_grossing_movies()
    # update_movie_videos()
    movies = Movie.objects.all()
    grossing = GrossingMovie.objects.all()
    header_movies = movies[:10]
    popular_movies_1 = movies[10:20]
    popular_movies_2 = movies[20:]
    context = {
        "header_movies": header_movies,
        "movies_1" : popular_movies_1,
        "movies_2" : popular_movies_2,
        "grossing": grossing,
    }
    return render(request, "core/index.html", context)

def movie_detail_view(request, tmdb_id):
    movie = Movie.objects.get(tmdb_id=tmdb_id)
    context = {
        "movie": movie,
        "star_rating": generate_star_html(movie.rating)
    }
    return render(request, "core/movie-detail.html", context)