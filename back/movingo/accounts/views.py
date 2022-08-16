# Create your views here.
from django.shortcuts import get_object_or_404
from django.contrib.auth import get_user_model

from rest_framework.decorators import api_view
from rest_framework.response import Response

from .serializers import ProfileSerializer, CurrentUserSerializer, ProfileInfoSerializer
from movies.serializers.movie import MovieSerializer
from .models import ProfileInfo
from movies.models import Review
from random import randint



User = get_user_model()
@api_view(['GET'])
def current_user(request):
    user = request.user
    if not ProfileInfo.objects.filter(user_id = user.pk).exists():
        rn = int(str(randint(1, 999999)).zfill(6))
        ProfileInfo.objects.create(user_id = user.pk, nickname=f"뉴비{rn}")
    serializer = CurrentUserSerializer(user)
    return Response(serializer.data)

@api_view(['GET', 'PUT'])
def profile(request, username):
    user = get_object_or_404(User, username=username)
    if request.method=="GET":
        serializer = ProfileSerializer(user)
        return Response(serializer.data)
    elif request.method=="PUT":
        if request.user == user:
            profile_info = get_object_or_404(ProfileInfo, user_id = user.pk)
            serializer = ProfileInfoSerializer(instance=profile_info, data=request.data)
            if serializer.is_valid(raise_exception=True):
                serializer.save()
                serializer = ProfileSerializer(user)
                return Response(serializer.data)

@api_view(['POST'])
def follow(request, user_pk): 
    user = get_object_or_404(get_user_model(), pk = user_pk)
    if user != request.user:
        if user.followers.filter(pk=request.user.pk).exists():
            user.followers.remove(request.user)
        else:
            user.followers.add(request.user)
        serializer = ProfileSerializer(user)
        return Response(serializer.data)


@api_view(['DELETE'])
def user_review(request, review_pk):
    review = get_object_or_404(Review, pk=review_pk)
    # movie_pk = Review.objects.filter(pk='review_pk').values('movie')
    # movie = get_object_or_404(Movie, pk=movie_pk)
    user = request.user
    def delete_user_review():
        if review.user.username == user.pk:
            review.delete()
            serializer = ProfileSerializer(user)
            return Response(serializer.data)
    
    if request.method == 'DELETE':
        return delete_user_review()

