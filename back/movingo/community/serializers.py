from rest_framework import serializers
from django.contrib.auth import get_user_model
from community.models import Thread, Comment
from accounts.models import ProfileInfo
from movies.models import Movie


User = get_user_model()
class UserSerializer(serializers.ModelSerializer):
    
    class ProfileInfoSerializer(serializers.ModelSerializer):

        class Meta:
            model=ProfileInfo
            fields = ('nickname', 'profile_img',)
    
    profile_info= ProfileInfoSerializer(many=True)

    class Meta:
        model = User
        fields = ('id', 'username', 'profile_info')

# Comment CRUD
class CommentSerializer(serializers.ModelSerializer):
    
    class UserSerializer(serializers.ModelSerializer):
    
        class ProfileInfoSerializer(serializers.ModelSerializer):

            class Meta:
                model=ProfileInfo
                fields = ('nickname', 'profile_img',)
        
        profile_info= ProfileInfoSerializer(many=True)

        class Meta:
            model = User
            fields = ('id', 'username', 'profile_info')
            
    user = UserSerializer(read_only=True)
    
    class Meta:
        model = Comment
        fields = ('pk', 'user', 'content', 'created_at', 'created_string' )
        read_only_fields = ('thread',)

# Tread List(메인 화면에 보여주기)
class MainThreadSerializer(serializers.ModelSerializer):

    class MovieSerializer(serializers.ModelSerializer):
        
        class Meta:
            model=Movie
            fields = ('id', 'title', 'poster_path', 'backdrop_path', )

    class CommentSerializer(serializers.ModelSerializer):
    
        user = UserSerializer(read_only=True)

        class Meta:
            model = Comment
            fields = ('pk', 'user', 'content', 'created_at', 'created_string' )
            read_only_fields = ('thread',)

    movie = MovieSerializer(read_only=True)
    comment_count = serializers.IntegerField()
    comments = CommentSerializer(many=True, read_only=True)

    class Meta:
        model= Thread
        fields= ('pk', 'movie', 'comment_count', 'comments')




# Thread READ
class ThreadSerializer(serializers.ModelSerializer):

    class CommentSerializer(serializers.ModelSerializer):
    
        class UserSerializer(serializers.ModelSerializer):
        
            class ProfileInfoSerializer(serializers.ModelSerializer):

                class Meta:
                    model=ProfileInfo
                    fields = ('nickname', 'profile_img',)
            
            profile_info= ProfileInfoSerializer(many=True)

            class Meta:
                model = User
                fields = ('id', 'username', 'profile_info')
                
        user = UserSerializer(read_only=True)
        
        class Meta:
            model = Comment
            fields = ('pk', 'user', 'content', 'created_at', 'created_string' )

    class MovieDataSerializer(serializers.ModelSerializer):

        class Meta:
            model = Movie
            fields = ('pk', 'title', 'poster_path', 'backdrop_path',)
    
    movie = MovieDataSerializer()
    comments = CommentSerializer(read_only=True, many=True)

    class Meta:
        model = Thread
        fields = ('pk', 'movie', 'comments')


# Thread Create
class ThreadCreateSerializer(serializers.ModelSerializer):

    movie = serializers.PrimaryKeyRelatedField(queryset=Movie.objects.all())

    class Meta:
        model = Thread
        fields = ('pk', 'movie')