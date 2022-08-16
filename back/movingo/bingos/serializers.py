from asyncore import read
from rest_framework import serializers
from .models import Bingo
from movies.models import Movie, Review

class BingoSerializer(serializers.ModelSerializer):
    
    class MovieSerializer(serializers.ModelSerializer):
        
        class ReviewSerializer(serializers.ModelSerializer):

            class Meta:
                model = Review
                fields = ('user', 'rate')

        reviews = ReviewSerializer(many=True, read_only=True)

        class Meta:
            model = Movie
            fields = ('id', 'title', 'poster_path', 'reviews')


    movies = MovieSerializer(many=True, read_only=True)

    class Meta:
        model = Bingo
        fields = ('pk', 'movies',)