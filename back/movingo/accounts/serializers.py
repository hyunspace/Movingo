from rest_framework import serializers
from django.contrib.auth import get_user_model
from movies.models import Movie, Review, Genre
from collects.models import Collection, Hashtag
from .models import ProfileInfo

# 회원가입 코드
from rest_framework import serializers


class CurrentUserSerializer(serializers.ModelSerializer):

    class ProfileInfoSerializer(serializers.ModelSerializer):
        
        class Meta:
            model = ProfileInfo
            fields = ('profile_img', 'nickname')

    profile_info = ProfileInfoSerializer(many=True)

    class Meta:

        model=get_user_model()
        fields = ('pk', 'username', 'profile_info')
        
class ProfileInfoSerializer(serializers.ModelSerializer):
        
    class Meta:
        model= ProfileInfo
        fields = ('pk', 'profile_img', 'nickname')

class ProfileSerializer(serializers.ModelSerializer):


    class MovieSerializer(serializers.ModelSerializer):
        
        class Meta:
            model = Movie
            fields = ('id', 'title', 'poster_path', 'original_title',)

    class ReviewSerializer(serializers.ModelSerializer):

        like_users_cnt = serializers.IntegerField(source='like_users.count', read_only = True)

        class MovieSerializer(serializers.ModelSerializer):
        
            class GenreSerializer(serializers.ModelSerializer):
                
                class Meta:
                    model = Genre
                    fields = ('id', 'name',)

            genres = GenreSerializer(many=True)

            class Meta:
                model = Movie
                fields = ('id', 'title', 'genres', 'poster_path')
        
        movie = MovieSerializer(read_only=True)

        class Meta:
            model = Review
            fields = ('pk', 'movie', 'rate', 'content', 'created_string', 'like_users_cnt',)
   
    class UserSerializer(serializers.ModelSerializer):

        class ProfileInfoSerializer(serializers.ModelSerializer):
        
            class Meta:
                model= ProfileInfo
                fields = ('profile_img', 'nickname')

        profile_info = ProfileInfoSerializer(many=True, read_only=True)

        class Meta:
            model= get_user_model()
            fields = ('id', 'username', 'profile_info')
    
    class CollectionSerializer(serializers.ModelSerializer):
        
        class MovieSerializer(serializers.ModelSerializer):

            class Meta:
                model=Movie
                fields = ('pk', 'title', 'poster_path', 'backdrop_path',)

        class UserSerializer(serializers.ModelSerializer):

            class Meta:
                model=get_user_model()
                fields = ('id', 'username',)
        
        class HashtagSerializer(serializers.ModelSerializer):
            class Meta:
                model = Hashtag
                field = ('tag',)

        like_cnt = serializers.IntegerField(source='like_users.count', read_only=True)
        like_users = UserSerializer(many=True, read_only=True)
        hashtags = HashtagSerializer(many=True, read_only=True)
        user = UserSerializer(read_only=True)
        movies = MovieSerializer(many=True)
        
    
        class Meta:
            model= Collection
            fields= ('pk', 'user', 'title', 'like_users', 'hashtags','description', 'like_cnt', 'movies',)
    
    class ProfileInfoSerializer(serializers.ModelSerializer):
        
        class Meta:
            model= ProfileInfo
            fields = ('profile_img', 'nickname')


    followers_cnt = serializers.IntegerField(source='followers.count', read_only = True)
    followings_cnt = serializers.IntegerField(source='followings.count', read_only = True)
    reviews_cnt = serializers.IntegerField(source='reviews.count', read_only = True)
    collections_cnt = serializers.IntegerField(source='collections.count', read_only = True)
    

    profile_info = ProfileInfoSerializer(many=True)
    wish_movies = MovieSerializer(many=True)
    collections = CollectionSerializer(many=True)
    like_collections = CollectionSerializer(many=True)
    reviews = ReviewSerializer(many=True)
    followers = UserSerializer(many=True)

    class Meta:
        model = get_user_model()
        fields = ('pk', 'username', 'profile_info', 'wish_movies', 'like_collections', 'followers', 'collections', 'reviews', 'followers_cnt', 'followings_cnt','reviews_cnt','collections_cnt',)

    
    
