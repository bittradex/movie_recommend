# import requests
# from decouple import config
# API_KEY = config("API_KEY")
# BASE_URL = 'https://api.themoviedb.org/3/'



# def get_popular_movies():
#     url = f'https://api.themoviedb.org/3/movie/popular?api_key={API_KEY}&language=en-US&page=2'
#     response = requests.get(url)
#     if response.status_code == 200:
#         return response.json()['results']
#     else:
#         return None


# def get_top_grossing_movies():
#     # Base URL for TMDB API
#     base_url = 'https://api.themoviedb.org/3'
    
#     # Discover movies
#     discover_url = f'{base_url}/discover/movie'
#     discover_params = {
#         'api_key': API_KEY,
#         'sort_by': 'popularity.desc',  # We can start by sorting by popularity or vote count
#     }
    
#     response = requests.get(discover_url, params=discover_params)
#     movies = response.json().get('results', [])
    
#     # Fetch detailed movie info to get revenue
#     movie_details = []
#     for movie in movies:
#         movie_id = movie['id']
#         movie_url = f'{base_url}/movie/{movie_id}'
#         movie_params = {
#             'api_key': API_KEY,
#         }
#         movie_response = requests.get(movie_url, params=movie_params)
#         movie_detail = movie_response.json()
#         movie_details.append(movie_detail)
    
#     # Sort movies by revenue
#     top_grossing_movies = sorted(movie_details, key=lambda x: x.get('revenue', 0), reverse=True)
    
#     # Get the top 10
#     top_10_movies = top_grossing_movies[:10]
    
#     return top_10_movies

# def get_other_movies(category='top_rated'):
#     url = f'https://api.themoviedb.org/3/movie/{category}?api_key={API_KEY}&language=en-US&page=1'
#     response = requests.get(url)
#     if response.status_code == 200:
#         return response.json()['results']
#     else:
#         return None

# def get_movie_credits(movie_id):
#     url = f'{BASE_URL}movie/{movie_id}/credits'
#     params = {
#         'api_key': API_KEY
#     }
#     response = requests.get(url, params=params)
#     if response.status_code == 200:
#         return response.json()
#     return None

# def get_movie_details(movie_id):
#     url = f'https://api.themoviedb.org/3/movie/{movie_id}?api_key={API_KEY}&language=en-US&append_to_response=release_dates'
#     response = requests.get(url)
#     if response.status_code == 200:
#         return response.json()
#     else:
#         return None

# def extract_movie_info(movie_data):
#     genres = [genre['name'] for genre in movie_data.get('genres', [])]
    
#     release_dates = movie_data.get('release_dates', {}).get('results', [])
#     content_rating = None
    
#     for country in release_dates:
#         if country['iso_3166_1'] == 'US':
#             for release_date in country['release_dates']:
#                 if 'certification' in release_date and release_date['certification']:
#                     content_rating = release_date['certification']
#                     break
#         if content_rating:
#             break

#     return {
#         'genres': genres,
#         'content_rating': content_rating
#     }
