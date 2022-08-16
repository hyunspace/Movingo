from collects.models import Collection
from rest_framework import serializers
from django.contrib.auth import get_user_model

from accounts.models import ProfileInfo

from ..models import Movie, Genre, Review
from accounts.models import ProfileInfo


class GenreSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Genre
        fields = ('pk', 'name',)

class MovieListSerializer(serializers.ModelSerializer):

    class UserSerializer(serializers.ModelSerializer):

        class Meta:
            model = get_user_model()
            fields = ('pk', 'username')

    wish_users = UserSerializer(many=True)
    genres = GenreSerializer(many=True)

    class Meta:
        model = Movie
        fields = ('pk', 'title', 'overview', 'poster_path', 'vote_average','original_title', 'wish_users', 'genres')


class MovieSerializer(serializers.ModelSerializer):

    class UserSerializer(serializers.ModelSerializer):

        class ProfileSerilizer(serializers.ModelSerializer):
            
            class Meta:
                model = ProfileInfo
                fields = ('profile_img', 'nickname')

        profile_info = ProfileSerilizer(many=True)

        class Meta:
            model = get_user_model()
            fields = ('pk', 'username', 'profile_info')

    class RelatesSerializer(serializers.ModelSerializer):

        class Meta:
            model = Movie
            fields = ('pk', 'title', 'poster_path',)

    class CollectionSerializer(serializers.ModelSerializer):
        
        class MovieCSerializer(serializers.ModelSerializer):
            
            class Meta:
                model = Movie
                fields= ('poster_path',)

        movies = MovieCSerializer(many=True)

        class Meta:
            model = Collection
            fields = ('pk', 'title', 'movies',)

    wish_users = UserSerializer(many=True)
    wish_count = serializers.IntegerField(source='wish_users.count', read_only=True)
    reviews_cnt = serializers.IntegerField(source='reviews.count', read_only=True)
    genres = GenreSerializer(many=True)
    related_movies = RelatesSerializer(many=True)
    collections = CollectionSerializer(many=True)

    class ReviewSerializer(serializers.ModelSerializer):

        class UserSerializer(serializers.ModelSerializer):
            
            class ProfileSerializer(serializers.ModelSerializer):
                
                class Meta:
                    model=ProfileInfo
                    fields=('pk', 'nickname')
            
            profile_info = ProfileSerializer(many=True)
            class Meta:
                model=get_user_model()
                fields=('pk', 'username', 'profile_info')

        like_users_cnt = serializers.IntegerField(source='like_users.count', read_only=True)
        user = UserSerializer(read_only=True)

        class Meta:
            model = Review
            fields = ('pk', 'user', 'rate', 'content', 'like_users_cnt', 'like_users')

    reviews = ReviewSerializer(many=True)

    class Meta:
        model = Movie
        fields = ('pk', 'title', 'overview', 'release_date', 'original_title','poster_path', 'backdrop_path', 'vote_average', 'reviews_cnt',
        'vote_count', 'popularity', 'adult', 'view_cnt', 'genres', 'related_movies', 'wish_users','wish_count', 'reviews', 'collections')

class AutoCompleteSerializer(serializers.ModelSerializer):

    class Meta:
        
        model=Movie
        fields=('title',)