from django.db import models
from userauths.models import User


class Movie(models.Model):
    tmdb_id = models.IntegerField(unique=True)
    title = models.CharField(max_length=200)
    overview = models.TextField()
    release_date = models.DateField()
    poster_path = models.CharField(max_length=200)
    backdrop_path = models.CharField(max_length=200)
    popularity = models.FloatField()
    genres = models.JSONField(default=list) 
    runtime = models.IntegerField(null=True, blank=True) 
    content_rating = models.CharField(max_length=10, null=True, blank=True) 
    rating = models.FloatField(null=True, blank=True)  # average rating
    starring_cast = models.JSONField(null=True, blank=True)
    video_url = models.CharField(max_length=255, null=True, blank=True) 
    release_date = models.DateField()

    def get_backdrop_url(self, size='w500'):
        base_url = 'https://image.tmdb.org/t/p/'
        return f"{base_url}{size}{self.backdrop_path}"
    def get_poster_url(self, size='w500'):
        base_url = 'https://image.tmdb.org/t/p/'
        return f"{base_url}{size}{self.poster_path}"


class GrossingMovie(models.Model):
    tmdb_id = models.IntegerField(unique=True)
    title = models.CharField(max_length=200)
    overview = models.TextField()
    release_date = models.DateField()
    poster_path = models.CharField(max_length=200)
    backdrop_path = models.CharField(max_length=200)
    popularity = models.FloatField()
    genres = models.JSONField(default=list) 
    runtime = models.IntegerField(null=True, blank=True) 
    content_rating = models.CharField(max_length=10, null=True, blank=True) 
    rating = models.FloatField(null=True, blank=True)  # average rating
    starring_cast = models.JSONField(null=True, blank=True)
    video_url = models.CharField(max_length=255, null=True, blank=True) 
    release_date = models.DateField()

    def get_backdrop_url(self, size='w500'):
        base_url = 'https://image.tmdb.org/t/p/'
        return f"{base_url}{size}{self.backdrop_path}"
    def get_poster_url(self, size='w500'):
        base_url = 'https://image.tmdb.org/t/p/'
        return f"{base_url}{size}{self.poster_path}"
    


class Review(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    rating = models.IntegerField()
    comment = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)