from rest_framework import serializers
from django.contrib.auth import get_user_model
from accounts.models import ProfileInfo
from ..models import Review, Movie

class ReviewSerializer(serializers.ModelSerializer):

    class UserSerializer(serializers.ModelSerializer):

        class ProfileSerilizer(serializers.ModelSerializer):
            
            class Meta:
                model = ProfileInfo
                fields = ('user', 'nickname')

        profile_info = ProfileSerilizer(many=True)
        class Meta:
            model = get_user_model()
            fields = ('pk', 'username', 'profile_info',)
            
    user = UserSerializer(read_only=True)
    like_users_cnt = serializers.IntegerField(source='like_users.count', read_only = True)

    class Meta:
        model = Review
        fields = ('pk', 'user', 'like_users_cnt', 'rate', 'content', 'created_string',)
        read_only_fields = ('movie', )