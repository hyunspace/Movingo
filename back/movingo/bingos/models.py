from django.db import models
from django.conf import settings
from movies.models import Movie

# Create your models here.
class Bingo(models.Model):
    current = models.BooleanField(default=False)
    movies = models.ManyToManyField(Movie, related_name='bingos')
